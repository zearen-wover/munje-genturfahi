{-
 -
 -}

module Main where

import System.Environment (getArgs)

import Text.Parsec

import Text.PEG

main = do
    (fn:_) <- getArgs
    txt <- readFile fn
    let res = parse peg fn txt
    print res
