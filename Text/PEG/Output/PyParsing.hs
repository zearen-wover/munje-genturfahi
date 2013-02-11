{-
 - Zachary Weaver <zearen.wover@gmail.com>
 - Text/PEG/Output/PyParsing.hs
 -
 - This is the output module to PyParsing.
 -}
{-# LANGUAGE FunctionalDependencies #-}
module Text.Peg.Output.PyParsing
    ( showPEG
    , showRule
    , showExpr
    , showForward
    , showsRule
    , showsExpr
    , showsForward
    , orderPEG
    , module Text.PEG
    )

import Data.List

import Text.PEG hiding (peg)
import Data.Dependency
import Util

HasDe

showRule :: Rule -> String
showRule = flip showsPEG []

showsRule :: Rule -> ShowS
showsRule (Rule (name, expr)) = (rule++) . (" = ") . showsExpr expr

showExpr :: Expr -> String
showExpr = flip showsExpr []

intersperses :: ShowS -> [ShowS] -> ShowS
intersperses sep ss =  foldl' (\acc x -> acc . sep . x) id ss

showsExpr :: Expr -> ShowS
showsExpr (XLit str) = ("Literal('"++) . (str++) . ("')"++)
showsExpr (XIdent str) = (str++)
showsExpr (XConcat xs) = intersperses (" + "++) map group $xs
  where group xalt@(XAlt _) = ("("++) . showsExpr xalt . (")"++)
        group expr = expr
showsExpr (XAlt xs) = intersperses (" | " ++) xs

showForward :: String -> String
showForward = flip showsForward []

showsForward :: String -> ShowS
showsForward str = (str++) . (" = Forward()"++)
