{-
 - Zachary Weaver <zearen.wover@gmail.com>
 - AKA Zearen Wover, ziren.uovr
 -
 - PEGParser.hs
 -
 - Creates a data model for the PEG grammar used for lojban so it
 - can be returned in various other parser formats, including
 -  PyPEG, Parsec, PEG.js, and XML
 -}


{-# LANGUAGE FlexibleContexts #-}
module PEGParser
    ( PEG(..)
    , Rule(..)
    , Expr(..)
    , peg
    ) where

import Control.Monad
import Control.Applicative ((<$>))

import qualified Data.Map as Map
import Data.Char
import Data.Maybe
import Data.List

import Text.Parsec


--------------------------------------------------------------------------------
-- Data Model
--------------------------------------------------------------------------------

type PEG = [Rule]

newtype Rule = Rule (String, Expr)
    deriving (Show, Eq)

data Expr = XLit String
          | XIdent String
          | XConcat [Expr]
          | XAlt [Expr]
          | XOpt Expr
          | X0More Expr
          | X1More Expr
          | XAnchor Expr
          | XNot Expr
          | XAny
          | XClass [Either Char (Char, Char)]
    deriving (Show, Eq)

--------------------------------------------------------------------------------
-- PEG Parsec Parser
--------------------------------------------------------------------------------

peg :: Stream s m Char => ParsecT s u m PEG
peg = do
    spaces
    fmap catMaybes $ line `manyTill` eof

line :: Stream s m Char => ParsecT s u m (Maybe Rule)
line = do
    ret <- (void comment >> return Nothing)
      <|> fmap Just rule
    spaces
    return ret


-- | Parses a line comment, and returns the comment's text
comment :: Stream s m Char => ParsecT s u m String
comment = do
    char ';'
    anyToken `manyTill` (void newline <|> eof)

-- | Parses a single rule.
-- Here, we line delineate rules
rule :: Stream s m Char => ParsecT s u m Rule
rule = do
    name <- identifier
    whitespace
    string "<-" 
    whitespace
    x <- expr $ void newline <|> eof
    return $ Rule (name, x)

-- | An identifier, either the LHS of a "<-", or a reference to a rule
-- in an expression
identifier :: Stream s m Char => ParsecT s u m String
identifier = many1 validChar
  where validChar = choice
           [ charRange 'a' 'z'
           , charRange 'A' 'Z'
           , charRange '0' '9'
           , char '-'
           ]

-- | Parses a PEG parsing expression.
-- 'endP' marks the end of an expression, for example a line end or a semi
expr :: Stream s m Char
    => ParsecT s u m ()
        -- ^ endP, the terminal expression
    -> ParsecT s u m Expr
expr endP = do
    -- We get the first atom
    thePrefix <- affix prefixes
    x <- fmap (applyAffix prefixes thePrefix) $ do
    -- We check for grouping first
        char '('
        whitespace
        expr $ void $ char ')'
    -- Otherwise, we see should have a single atom
      <|> atom
    theSuffix <- affix suffixes
    let x' = applyAffix suffixes theSuffix x
    whitespace
    -- Next, lets see if we have an alternation
    try (xAlt x')
    -- Else, we look for a concatenation
      <|> try (xConcat x')
    -- If all else fails, we should be at the end of an expression
      <|> do
        endP
        return x'
  where affix affixes = try (oneOf $ Map.keys affixes) <|> return ' '
        applyAffix affixes = fromMaybe id . flip Map.lookup affixes
        prefixes = Map.fromList
            [ '!' >< XNot
            , '&' >< XAnchor
            ]
        suffixes = Map.fromList
            [ '?' >< XOpt
            , '*' >< X0More
            , '+' >< X1More
            ]
        atom = choice
            [ xLit
            , xIdent
            , xAny
            , xClass
            ]
        xAlt x = do
            char '/'
            whitespace
            xTail <- expr endP
            return . XAlt . (x:) $ case xTail of
                XAlt alts -> alts
                _ -> [xTail]
        xConcat x = do
            whitespace
            xTail <- expr endP
            return . XConcat . (x:) $ case xTail of
                XConcat cats -> cats
                _ -> [xTail]

xLit :: Stream s m Char => ParsecT s u m Expr
xLit = fmap XLit $ xLit' '"' <|> xLit' '\''
  where xLit' delim = do
            char delim
            xChar `manyTill` try xCharNotDelim
          where xCharNotDelim = do
                    r@(ch, esc) <- xCharTrack
                    if ch == delim && not esc
                      then return r
                      else fail "expected delim"

xIdent :: Stream s m Char => ParsecT s u m Expr
xIdent = fmap XIdent identifier

xAny :: Stream s m Char => ParsecT s u m Expr
xAny = do
    char '.'
    return XAny

xClass :: Stream s m Char => ParsecT s u m Expr
xClass = do
    char '['
    hasBracket <- (char ']' >> return True) <|> return False
    hasHyphen <- (char '-' >> return True) <|> return False
    classes <- xRange `manyTill` char ']'
    return . XClass
        $ ((Left ']':)??id) hasBracket
        $ ((Left '-':)??id) hasHyphen
        $ classes
  where xRange :: Stream s m Char => ParsecT s u m (Either Char (Char, Char))
        xRange = do
            openChar <- xChar
            do 
                char '-'
                closeChar <- xChar
                when (closeChar == '-') $ fail
                    "Got invalid range: ends with \'-\'"
                when (openChar >= closeChar) $ fail 
                    $ "Got invalid range: \'" 
                    ++ openChar : "\'>=\'" ++ closeChar : "\'"
                return $ Right (openChar, closeChar)
              <|> (return $ Left openChar)

--------------------------------------------------------------------------------
-- Utilities
--------------------------------------------------------------------------------

-- | This parses out escape characters in literals and chacter classes
-- We track whether it came from an 
xCharTrack :: Stream s m Char => ParsecT s u m (Char, Bool) 
xCharTrack = 
    do 
        char '\\'
        fmap (>< True) escapeSequence
    <|> fmap (>< False) anyToken
  where escapeSequence =
            do 
                char 'u'
                fmap (chr . readHex) $ count 4 hexDigit
            <|> do
                ch <- anyToken
                return $ fromMaybe ch $ Map.lookup ch specialChars
        specialChars = Map.fromList
            [ 'n' >< '\n'
            , 't' >< '\t'
            , 'r' >< '\r'
            ]

readHex :: String -> Int
readHex = foldl' acc 0
  where acc num dig = 16 * num + hexFromChar dig
        hexFromChar ch
            | '0' <= ch && ch <= '9' = ord ch - ord '0'
            | 'A' <= ch && ch <= 'F' = ord ch - ord 'A' + 10
            | 'a' <= ch && ch <= 'f' = ord ch - ord 'a' + 10
            | otherwise = error "Asked to parse non hexDigit"

xChar :: Stream s m Char => ParsecT s u m Char
xChar = fmap fst xCharTrack

whitespace :: Stream s m Char => ParsecT s u m String
whitespace = many $ oneOf " \t"

range :: (Ord o, Show o, Stream s m o) => (o -> Bool) -> o -> o -> ParsecT s u m o
range isNewLine startO endO =  tokenPrim show nextPos checkRange
  where nextPos pos t _ = 
            if isNewLine t then incSourceLine pos 1 else incSourceColumn pos 1
        checkRange ch = if startO <= ch && ch <= endO then Just ch else Nothing

charRange :: Stream s m Char => Char -> Char -> ParsecT s u m Char
charRange = range (=='\n')

(><) :: a -> b -> (a, b)
a >< b = (a, b)
infix 0 ><

(??) :: a -> a -> Bool -> a
(left ?? right) tf = if tf then left else right
infix 1 ??

--------------------------------------------------------------------------------
-- Shortcuts for debugging
--------------------------------------------------------------------------------

doParse p = parse p ""

