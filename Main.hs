{-
 - Zachary Weaver <zearen.wover@gmail.com>
 - AKA Zearen Wover, ziren.uovr
 -
 - Main.hs
 -
 - The entry point, right now uniquely for testing.
 -}

module Main where

import System.Environment (getArgs)

import Text.Parsec

import Text.PEG

main = do
    args <- getArgs
    txt <- if null args
        then getLine
        else readFile $ head args
    let res = parse peg fn txt
    print res
