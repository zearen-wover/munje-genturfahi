{-
 - Zachary Weaver <zearen.wover@gmail.com>
 - AKA Zearen Wover, ziren.uovr
 -
 - Main.hs
 -
 - The entry point, right now uniquely for testing.
 -}

{-# LANGUAGE FunctionalDependencies #-}
module Main where

import System.Environment (getArgs)

import Text.Parsec

import Data.Dependency
import Text.PEG
import Util

newtype IntDep = IntDep (Int, [Int])
    deriving (Show)

instance HasDependencies IntDep Int where
    name (IntDep (n,_)) = n
    dependencies (IntDep (_,ds)) = ds

main = main2

loadPeg = do
    args <- getArgs
    txt <- if null args
        then getLine
        else readFile $ head args
    return $ parse peg ((""??head args) $ null args) txt

main0 = loadPeg

main1 = do
    let (satOrd, mutRec) = orderDependencies depList
    putStrLn "Satisfied order"
    mapM_ print satOrd
    putStrLn "Mutually recursive"
    mapM_ print mutRec
  where depList = map IntDep $
            [ 3  >< [1,2]
            , 2  >< [1]
            , 1  >< []
            , 6  >< []
            , 4  >< [5]
            , 5  >< [4]
            ]
