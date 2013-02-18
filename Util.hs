{-
 - Zachary Weaver <zearen.wover@gmail.com>
 - Util.hs
 -
 - Provides utilities that are independent of all other modules
 -}

module Util 
    ( (.:)
    , (??)
    , (><)
    , loop
    ) where

(.:) :: (c -> d) -> (a -> b -> c) -> a -> b -> d
(.:) = (.).(.)
infixr 9 .:

(??) :: a -> a -> Bool -> a
(left ?? right) tf = if tf then left else right
infix 1 ??

(><) :: a -> b -> (a, b)
a >< b = (a, b)
infix 0 ><

loop :: Monad m => m Bool -> m ()
loop act = act >>= (loop act ?? return ())
