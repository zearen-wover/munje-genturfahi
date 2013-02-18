{-
 - Zachary Weaver <zearen.wover@gmail.com>
 - Text/PEG/Output/PyParsing.hs
 -
 - This is the output module to PyParsing.
 -}

{-# LANGUAGE FunctionalDependencies #-}
{-# LANGUAGE FlexibleInstances #-}
module Text.PEG.Output.PyParsing
    ( convertIdent
    , showPEG
    , showsPEG
    , showRule
    , showForwardRule
    , showExpr
    , showForward
    , showsForwardRule
    , showsExpr
    , showsForward
    , orderPEG
    , module Text.PEG
    ) where

import Data.List
import Data.Either

import Text.PEG hiding (peg)
import Data.Dependency
import Util

instance HasDependencies Rule [Char] where
    name (Rule (n, _)) = n
    dependencies (Rule (_, expr)) = getDeps expr
      where getDepsExprs = foldl' (flip (++)) [] . map getDeps
            getDeps (XIdent dep) = [dep]
            getDeps (XLit _) = []
            getDeps XAny = []
            getDeps (XClass _) = []
            getDeps (XOpt x) = getDeps x
            getDeps (X0More x) = getDeps x
            getDeps (X1More x) = getDeps x
            getDeps (XAnchor x) = getDeps x
            getDeps (XNot x) = getDeps x
            getDeps (XConcat xs) = getDepsExprs xs
            getDeps (XAlt xs) = getDepsExprs xs

convertIdent = map replaceChar
  where replaceChar ch
            | ch == '-' = '_'
            | otherwise = ch

showRule :: Rule -> String
showRule = flip showsRule []

showsRule :: Rule -> ShowS
showsRule (Rule (name, expr)) = (convertIdent name++) . (" = "++) . showsExpr expr

showForward :: String -> String
showForward = flip showsForward []

showsForward :: String -> ShowS
showsForward str = (convertIdent str++) . (" = Forward()"++)

showForwardRule :: Rule -> String
showForwardRule = flip showsForwardRule []

showsForwardRule :: Rule -> ShowS
showsForwardRule (Rule (name, expr)) = (convertIdent name++) . (" << ("++) . showsExpr expr . (")"++)

showExpr :: Expr -> String
showExpr = flip showsExpr []

intersperses :: ShowS -> [ShowS] -> ShowS
intersperses sep ss =  foldl1' (\acc x -> acc . sep . x) ss

showsExpr :: Expr -> ShowS
showsExpr (XLit str) = ("Literal('"++) . (str++) . ("')"++)
--showsExpr (XIdent str) = ("Group('"++) . (convertIdent str++) . ("')"++)
showsExpr (XIdent str) = (convertIdent str++)
showsExpr (XConcat xs) = intersperses (" + "++) $ map group $ xs
  where group xalt@(XAlt _) = ("("++) . showsExpr xalt . (")"++)
        group expr = showsExpr expr
showsExpr (XAlt xs) = intersperses (" | " ++) $ map showsExpr xs
showsExpr (XOpt expr) = ("Optional("++) . showsExpr expr . (")"++)
showsExpr (X0More XAny) = ("Empty()"++)
showsExpr (X0More expr) = ("ZeroOrMore("++) . showsExpr expr . (")"++)
showsExpr (X1More expr) = ("OneOrMore("++) . showsExpr expr . (")"++)
showsExpr (XAnchor expr) = ("FollowedBy("++) . showsExpr expr . (")"++)
showsExpr (XNot XAny) = ("StringEnd()"++)
showsExpr (XNot expr) = ("~"++) . case expr of
    (XConcat _) -> ("("++) . showsExpr expr . (")"++)
    (XAlt _) -> ("("++) . showsExpr expr . (")"++)
    _ -> showsExpr expr
showsExpr XAny = ("Regex('.')"++)
showsExpr (XClass ranges) = ("Regex('["++) . foldl' rangeS id ranges . ("]')"++)
  where rangeS acc (Left c) = acc . (c:)
        rangeS acc (Right (cs, ce)) = acc . (cs:) . ('-':) . (ce:)

orderPEG :: PEG -> ([Rule], [Rule])
orderPEG = orderDependencies . lefts

showPEG :: PEG -> String
showPEG = flip showsPEG []

showsPEG :: PEG -> ShowS
showsPEG thePEG = foldl' (.) id (map ((.('\n':)) . showsRule) sats)
    . foldl' (.) id (map ((.('\n':)) . showsForward . name) recs)
    . foldl' (.) id (map ((.('\n':)) . showsForwardRule) recs)
  where (sats, recs) = orderPEG thePEG
