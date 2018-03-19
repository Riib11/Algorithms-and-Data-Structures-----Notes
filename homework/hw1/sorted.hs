data SortedList a = SortedList [a]

instance Show a => Show (SortedList a) where
    show (SortedList xs) = "s" ++ show xs

sortedCons :: Ord a => a -> SortedList a -> SortedList a
sortedCons x (SortedList []) = singleton x
sortedCons x (SortedList (y:ys)) = if x <= y
    then SortedList (x:y:ys)
    else sortedCons y (sortedCons x $ SortedList ys)

sortedNil :: Ord a => SortedList a
sortedNil = SortedList []

singleton :: Ord a => a -> SortedList a
singleton x = SortedList [x]

toSortedList :: Ord a => [a] -> SortedList a
toSortedList [] = sortedNil
toSortedList (x:xs) = sortedCons x $ toSortedList xs