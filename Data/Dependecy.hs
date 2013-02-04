{-
 - Zachary Weaver <zearen.wover@gmail.com>
 - AKA Zearen Wover, ziren.uovr
 -
 - Data/Dependency.hs
 -
 - This is a utility for Text.PEG.Output.PyParsing.  It allows one to output
 - in order of no dependencies to most dependencies, and get the set of
 - mutually recursive rules.  It's generic because tu'a Haskell
 -}

{-# LANGUAGE FunctionalDependencies #-}
{-# LANGUAGE TemplateHaskell #-}
module Data.Dependency
    ( HasDependencies(..)
    ) where

import Control.Monad.State.Strict

import qualified Data.Map as Map
import qualified Data.Set as Set

import Data.Lens.Strict
import Data.Lens.Template

type Map = Map.Map
type Set = Set.Set

data Dependency a n = Dependency
    { item :: a
    , deps :: Set n
    }

data DepState a n = DepState
    { _known :: Set n
    , _remaining :: Map n (Dependency a n)
    , _output :: [a] -> [a]
    }

makeLens ''DepState

class Ord n => HasDependencies a n | a -> n where
    name :: a -> n
    dependencies :: a -> [n]

satisfied :: HasDependencies

collectSatisfied :: HasDependencies a n => State (DepState a n) Bool
collectSatisfied = do
    isSat <- fmap satisfies $ access known
    let (sat, unSat) = Map.partition partFun 
    
    return True
