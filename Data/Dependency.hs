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
{-# LANGUAGE ScopedTypeVariables #-}
module Data.Dependency
    ( HasDependencies(..)
    , Dependency(..)
    , satisfied
    , collectSatisfied
    , orderDependencies
    ) where

import Control.Monad.State.Strict

import qualified Data.Map as Map
import qualified Data.Set as Set

import Util

type Map = Map.Map
type Set = Set.Set

data Dependency a n = Dependency
    { item :: a
    , deps :: Set n
    }

data DepState a n = DepState
    { known :: Set n
    , remaining :: Map n (Dependency a n)
    , output :: [a] -> [a]
    }


class Ord n => HasDependencies a n | a -> n where
    name :: a -> n
    dependencies :: a -> [n]

satisfied :: HasDependencies a n => Set n -> Dependency a n -> Bool
satisfied knowns = flip Set.isSubsetOf knowns . deps

collectSatisfied :: HasDependencies a n => State (DepState a n) Bool
collectSatisfied = do
    isSat <- fmap (satisfied . known) get
    (sat, unSat) <- fmap (Map.partition isSat . remaining) get
    modify $ \d -> d{remaining = unSat}
    modify $ \d -> d{known = known d `Set.union` Set.fromList (Map.keys sat)}
    modify $ \d -> d{output = output d . ((map item $ Map.elems sat) ++)}
    return $ not $ Map.null sat
    

orderDependencies :: HasDependencies a n => [a] -> ([a], [a])
orderDependencies deps = flip evalState initState $ do
    loop collectSatisfied
    outs <- fmap output get
    rems <- fmap (map item . Map.elems . remaining) $ get
    return (outs [], rems)
  where aToEntry an'a =
            ( name an'a
            , Dependency
                { item = an'a
                , deps = Set.fromList $ dependencies an'a
                }
            )
        initState = DepState
            { known = Set.empty
            , remaining = Map.fromList $ map aToEntry deps
            , output = id
            }

