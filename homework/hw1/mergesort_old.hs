mergesort :: Ord a => [a] -> [a]
mergesort xs = helper xs 0 l
    where l = length xs

helper :: Ord a => [a] -> Int -> Int -> [a]
helper xs0 s f = if s<f-1
    then merge xs2 s m f
    else xs2
    where
        xs2 = helper xs1 m f
        xs1 = helper xs0 s m
        m   = (+) s $ div (f-s) 2

merge :: Ord a => [a] -> Int -> Int -> Int -> [a]
merge xs s m f =
    let
        putNext :: Int -> Int -> Int -> [a] -> 
        helper :: [a] -> Int -> Int -> Int -> [a]
        helper ys _  _  0 = ys
        helper ys p1 p2 i = helper zs p1' p2' (i-1)
            where
                zs, p1', p2' =
                    if      p1 >= m  then copyTo xs ys2, p1,   p2+1
                    else if p2 >= f  then copyTo xs ys1, p1+1, p2
                    else if y1 >= y2 then copyTo xs ys2, p1,   p2+1
                    else                  copyTo xs ys1, p2+1, p2
                ys1 = take 
    in
        helper xs s m (f-s)

copyTo :: Int -> [a] -> [a] -> [a]
copyTo 0 (x:xs) (y:ys) = x : ys
copyTo i (x:xs) (y:ys) = y : copyTo (i-1) xs ys

elemAt :: Int -> [a] -> a
elemAt 0 (x:xs) = x
elemAt i (x:xs) = elemAt (i-1) xs