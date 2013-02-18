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
import Text.PEG.Output.PyParsing
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
    case parse peg ((""??head args) $ null args) txt of
        (Left err) -> fail $ show err
        (Right thePeg) -> return thePeg

main0 = loadPeg >>= print

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

main2 = do
    thePeg <- loadPeg
    putStrLn $ showPEG thePeg
