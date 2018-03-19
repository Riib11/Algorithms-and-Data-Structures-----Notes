# Iterative Mergesort

Henry Blanchette

## Python Program:

```

from math import *
from random import shuffle

def mergesort (A):
    
    # auxillary array
    B = [ a for a in A ]

    # sweeps with incrementally doubling sizes
    size = 1
    len_a = len(A)
    while size < len_a:

        # extra hanging off the end
        len_extra = len_a % (size*2)

        # sweep across A with (size*2)-steps
        for i in range (0, len_a-len_extra, size*2):
            merge (A, B, i, i+size, i+2*size)

        # update A
        copyback (B, A)

        # merge in extra (I'm guessing this isn't the optimal way)
        for i in range (len_a-len_extra, len_a):
            merge (A, B, 0, i, i+1)
            copyback (B, A)

        # increment size
        size *= 2


def merge (A, B, start, middle, finish):
        
    # pointers in left and right half of A
    pointers = { "left": start, "right": middle }

    # fill in next A index with a pointer's target
    # increments pointer
    def put_next (p, i):
        B[i] = A[pointers[p]]
        pointers[p] += 1

    # fill in section of B
    for i in range (start, finish):
        left, right = pointers["left"], pointers["right"]

        if   (left >= middle):      next = "right"
        elif (right >= finish):     next = "left"
        elif (A[left] >= A[right]): next = "right"
        else:                       next = "left"

        put_next (next, i)


def copyback (B, A):
    for i in range(len(B)): A[i] = B[i]

```

## Python Test

### Testing Program

```
from mergesort2 import mergesort
import random
from copy import deepcopy
random.seed()

# main

def main():

    # inputs
    test_count      = 30
    test_lengths    = [ random.randint(1,10) for _ in range(test_count) ]
    test_inputs     = [ makePermutation(l) for l in test_lengths ]

    # outputs
    test_outputs    = deepcopy (test_inputs)
    for ls in test_outputs: mergesort (ls)

    # log
    print("----------------------------------------------------------------------")
    print("| Sorted? | input -> output")
    print("----------------------------------------------------------------------")
    for i in range (test_count):
        print ("| ",checkSorted(test_outputs[i]),"  |", # success?
            test_inputs[i],"->",test_outputs[i]) # log
    print("----------------------------------------------------------------------")

# utility functions

def makeList (l):
    return [ i for i in range(l) ]

def makePermutation (l):
    ls = makeList(l)
    random.shuffle(ls)
    return ls

def checkSorted (ls):
    for i in range(len(ls)-1):
        if ls[i] > ls[i+1]: return False
    return True

# run

main()
```

### Testing Results

```
----------------------------------------------------------------------
| Sorted? | input -> output
----------------------------------------------------------------------
|  True   | [0, 1, 2, 5, 4, 3] -> [0, 1, 2, 3, 4, 5]
|  True   | [1, 0] -> [0, 1]
|  True   | [0, 1] -> [0, 1]
|  True   | [0] -> [0]
|  True   | [4, 1, 2, 3, 6, 5, 0] -> [0, 1, 2, 3, 4, 5, 6]
|  True   | [4, 0, 5, 1, 2, 3] -> [0, 1, 2, 3, 4, 5]
|  True   | [1, 0, 3, 2] -> [0, 1, 2, 3]
|  True   | [5, 3, 0, 4, 1, 2] -> [0, 1, 2, 3, 4, 5]
|  True   | [5, 1, 0, 4, 3, 2] -> [0, 1, 2, 3, 4, 5]
|  True   | [3, 6, 7, 4, 8, 5, 0, 2, 1] -> [0, 1, 2, 3, 4, 5, 6, 7, 8]
|  True   | [1, 2, 6, 0, 5, 3, 4] -> [0, 1, 2, 3, 4, 5, 6]
|  True   | [0, 4, 3, 2, 1] -> [0, 1, 2, 3, 4]
|  True   | [2, 1, 0, 3] -> [0, 1, 2, 3]
|  True   | [3, 2, 1, 0] -> [0, 1, 2, 3]
|  True   | [3, 2, 4, 0, 6, 5, 1] -> [0, 1, 2, 3, 4, 5, 6]
|  True   | [0, 5, 1, 6, 4, 7, 2, 3] -> [0, 1, 2, 3, 4, 5, 6, 7]
|  True   | [4, 3, 1, 2, 0] -> [0, 1, 2, 3, 4]
|  True   | [0, 5, 2, 4, 3, 1] -> [0, 1, 2, 3, 4, 5]
|  True   | [1, 2, 0, 3] -> [0, 1, 2, 3]
|  True   | [1, 0, 3, 2] -> [0, 1, 2, 3]
|  True   | [5, 0, 3, 2, 4, 1] -> [0, 1, 2, 3, 4, 5]
|  True   | [0, 5, 6, 3, 2, 4, 1] -> [0, 1, 2, 3, 4, 5, 6]
|  True   | [1, 6, 0, 4, 2, 5, 3] -> [0, 1, 2, 3, 4, 5, 6]
|  True   | [2, 0, 1, 6, 5, 3, 4] -> [0, 1, 2, 3, 4, 5, 6]
|  True   | [5, 2, 3, 1, 4, 0] -> [0, 1, 2, 3, 4, 5]
|  True   | [2, 1, 5, 6, 0, 3, 4] -> [0, 1, 2, 3, 4, 5, 6]
|  True   | [1, 2, 0] -> [0, 1, 2]
|  True   | [5, 7, 6, 0, 2, 3, 4, 8, 1] -> [0, 1, 2, 3, 4, 5, 6, 7, 8]
|  True   | [3, 0, 2, 1] -> [0, 1, 2, 3]
|  True   | [6, 2, 8, 4, 5, 0, 7, 1, 3] -> [0, 1, 2, 3, 4, 5, 6, 7, 8]
----------------------------------------------------------------------
[Finished in 0.1s]
```

## Haskell Program

(Much more pretty)

```
merge :: Ord a => [a] -> [a] -> [a]
merge xs [] = xs
merge [] ys = ys
merge (x:xs) (y:ys)
    | x <= y    = x : merge xs (y:ys)
    | otherwise = y : merge (x:xs) ys

mergesort :: Ord a => [a] -> [a]
mergesort [] = []
mergesort [x] = [x]
mergesort xs = merge (halfsort take) (halfsort drop)
    where halfsort side = mergesort $ side mid xs
          mid = div (length xs) 2
```