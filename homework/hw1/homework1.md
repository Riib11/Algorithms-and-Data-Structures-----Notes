# Algorithms - Homework 1

Henry Blanchette

## Problem 1

Let `A[1..n]` be an array of integers. Let `I(A) = { (j,i) | j < i and A[j] > A[i] }` be the set of inversions in A.

### a)

Let `A = [8,6,1,3,4]`. Then `I(A) = { (1,2), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5) }`.

### b)

We found that the running time of insertion-sort was

```
T(n) = c1 + c2 n + c3 * sum ([i | i in [0..n-1]])
// c1, c2, c3 are costs
```

### c)

`|I(A)|` is minimized when `A` is sorted, for no index pairs will have out of order values so `|I(A)| == 0`. `|I(A)|` is maximized when `A` is in reverse order, for all index pairs will be out of order so `|I(A)| == n choose 2`.

### d)

For any neighbor swap-based algorithm, the lower bound on the number of swaps will be `0` since in the best case the list is sorted. Additionally, the lower bound on the run time will be asymptotically linear for the algorith must compare `n-1` neighboring pairs which will all be in order.

### e)

Pseudocode:

```
// counts inversions during mergesorting A
mergesort (A) := {
    helper (A, new array|A|, 0, |A|)
}

// counts inversions during mergesorting A[start:finish]
helper (A, B, start, finish) := {
    inversions := 0

    // not sorted
    if (finish - start > 0) {
        middle := start + floor ( (finish-start)/2 )
        inversions += helper (A, B, start, middle)
        inversions += helper (A, B, middle, finish)
        inversions += merge  (A, B, start, middle, finish)
    }

    copyback (B, A)
    return inversions
}

// counts inversions during sorting merge
merge (A, B, start, middle, finish) := {

    pointers = { "left": start, "right": middle }
    inversions = 0

    // fills in next A index with a pointer's target
    // also increments the pointer
    put_next (p, i) := {
        B[i] = A[ pointers[p] ]
        pointers[p] ++
    }

    // fill in section of B
    for (i in [start..finish-1]) {
        left, right =
            pointers["left"], pointers["right"]

        next = switch {
            left    >= middle   -> "right",
            right   >= finish   -> "left",
            A[left] >= A[right] -> {
                inversions ++
                return "right"
            }
            True                -> "left"
        }

        put_next(next, i)
    }

    copyback (B, A)
    return inversions
}

// copy B into A
copyback(B, A) := for (i in [0..|A|-1]) {
    A[i] = B[i]
}
```

## CLRS 2.2 - 2

2.2-2

Consider sorting n numbers stored in array A by first finding the smallest element of A and exchanging it with the element in A[1] . Then find the second smallest element of A, and exchange it with A[2]. Continue in this manner for the first n-1 elements of A. Write pseudocode for this algorithm, which is known as selection sort. What loop invariant does this algorithm maintain? Why does it need to run for only the first n   1 elements, rather than for all n elements? Give the best-case and worst-case running times of selection sort in ‚(big Theta)-notation.

Pseudocode:

```
selectionsort (A) := {

    // loop through n-1 indecies of A
    for (i in [0..|A|-2]) {

        // find ith smallest element of A
        curr_min := A[i]
        curr_ind := i
        for (j in [i+1..|A|-1]) {
            if (A[j] <= curr_min) {
                curr_min = A[j]
                curr_ind = j
            }
        }

        // switch the ith smallest element with A[i]
        A[j] = A[i]
        A[i] = curr_min
    }
}
```

This algorithm maintains `A[i..j-1]` as loop invariant.

Selection-sort only needs to loop through and order the first `n-1` of the new, ordered `A` because if the last element, in order to have ended up being the last element, will have to not be less than any of the previous `ith` smallest elements, so it must be the largest (by the `>=` relation).

In the best case, selection-sort will check `n-2` pairs in the first iteration, `n-3` pairs in the second, and etc for `n-1` iterations. In total there will be `1 + 2 + ... + (n-2) = (n-2)(n-1)/2 = n^2/2 - (3 n)/2 + 1` checks, and no switches. This will be `Θ(n^2)` running time.

In the worst case, the list will be in reverse order. So, there will be just as many checks as before, but there will be an additional operation - a switch - each iteration. Treating checks and switches as having the same cost yeilds `[ n^2/2 - (3 n)/2 + 1 ] + [ n-1 ] = n^2/2 - (n/2)` operations, since there are `n-1` iterations. This will still be `Θ(n^2)` running time.


## Problem 3

Pseudocode:

```
mergesort (A) := {

    // auxillary array
    B = new array[|A|]

    // sweeps with incrementally doubling sizes
    size := 1
    while (size < |A|) {

        // sweep across A in sized chunks
        for (i in [0..|A|-1] with (step = size*2)) {
            merge (A, B, i, i+size, i+2*size)
        }

        // update A
        copyback (B, A)
        // increment size
        size *= 2
    }
}

merge (A, B, start, middle, finish) := {

    pointers = { "left": start, "right": middle }

    // fills in next A index with a pointer's target
    // also increments the pointer
    put_next (p, i) := {
        B[i] = A[ pointers[p] ]
        pointers[p] ++
    }

    // fill in section of B
    for (i in [start..finish-1]) {
        left, right =
            pointers["left"], pointers["right"]

        next = switch {
            left    >= middle   -> "right",
            right   >= finish   -> "left",
            A[left] >= A[right] -> "right"
            True                -> "left"
        }

        put_next(next, i)
    }
}

// copy B into A
copyback(B, A) := for (i in [0..|A|-1]) {
    A[i] = B[i]
}
```