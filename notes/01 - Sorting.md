# Sorting

"in-place" sorting. Rearranging values in **computer's memeory**.

Computer's memory: **Arrays**
- fixed-length sequence in memory
- accessible by index
- variable that stores the "Array" is a pointer

Given:
- An array `A` with length `n` of sequence `a.1,a.2,a.3,...,a.n in Integers`.
- `A[i] = a.i, where i in {1..n}`

Goal:
- Rearrange `A[1..n]` acc to a permutation `pi : {1..n} -> {1..n}`.
- Such that `a.(pi(1)) <= a.(pi(2)) <= ... <= a.(pi(n))`.
- Such that, after running the algorithm, `A[i] = a.(pi(i)) where i in {1..n}`.

## Insertion Sort

### Idea

In progress sorting till done. Have a pointer at `i`, and have everything to hte left of `i` be sorted and everything to the right of `i` be unsorted. Step `i` to the right until eventually everything will be sorted when `i` reaches the furthest right.

### Psuedocode

```
insertionSort (A) := {
    n := |A|
    for (i in [1..n]) {
        j := i - 1
        while (j>0 && A[j]>A[j+1]) {
            swap (A[j], A[j+1])
            j--
        }
    }
}
```

### Proof

Case analysis, induction.

### Runtime Analysis

- Estimate the cost of operations executed.
- Make reasonable assumptions about portion of code's execution time.
- Imagine performance "for all A's" => scale by parameters; `runtime(n) where |A| = n`.
- Count # of specific operations

```
    t.i = # of swaps performed to palce A[i]
    
    T(A) = running time of insertion-sort on array A
         = d1 + d2 n + d3 sum([t.i for i in [1..n]])
            where t = [0..n-1]

    lower bound <=  formula <= upper bound
    d1 + d2 n   <=  T(A)    <= d1 + d2 n + d3 sum([t.i for i in [1..n]])
        where sum([t.i for i=0..n-1]) = n(n-1)/2 = n^2/2 - n/2

    so could take quadratic time! (from the n^2)

```

### Worst Case

`W(n) = max([T(A) for |A|==n])`. In the case of insertion-sort, `W(n) = Θ(n^2)` (big Θ notation), which means the worst case scales quadratically.

Additionally, `T(A) = O(n^2)` (big O notation) means that insertion-sort is "no worse than quadratic".

## Representative Operations

Ways to measure stuff happening in an algorithm

- \# of comparisons made
- \# of array accesses
- \# of swaps
- \# of instructions

## Merge Sort

### Idea

Based on merge. Take two adjacent sections in original array, each of which are sorted. Then merge them together in auxillary array in such a way that they end up sorted together.

Ex:

```
mergeSort([2, 8, 12,],[1, 9, 11,])
= 2>1   -> 1
: 2<9   -> 2
: 8<9   -> 8
: 12>9  -> 9
: 12>11 -> 11
: 12    -> [12]
-> [1,2,8,9,11,12]
```

### Psuedocode

```
mergeSort (A) := {
    B := new array
    helper(A,B,0,n)
}

helper (A,B,l,r) := {
    if (r-l > 1) {
        m := ceil $ (l+1)/2     // Array assignments count:
        helper(A,B,l,m)         // C(ceil(n/2))
        helper(A,B,m,r)         // C(ceil(n-2))
        merge(A,B,l,m,r)        // n
        copy_back(B,A,l,r)      // n
    } else {
        // length 1 list already sorted!
    }
}

marge (A,B,l,m,r) := {
    i,j := l,m
    for (k in [l..r-1]) {
        if (j >= r) {
            B[k] = A[i]
            i++
        } else if ( i>= m) {
            B[j] = A[j]
            j++
        } else if (A[i] <= A[j]) {
            B[k] = A[i]
            i++
        } else {
            B[j] = A[j]
            j++
        }
    }
}
```

### Runtime Analysis

Because `helper` is recursive, return count is governed by recurrence.

```
    C(n) := case n of 
        0,1 -> 0
        n>1 -> C(ceil(n/2)) + C(floor(n/2)) + 2 n
```

Recursive algorithms tend to lead to recurrences in their running time formula. But, for this to make more sense, we need to solve the recurrence:

- Guess and check (proof by induction)
- Substitution
- Recursion tree
- Master Method ®

Assume `n = 2^p` for some `p >= 0` (allows for equal sized subportions). Also assume that `n` is large, initially. Since `n` is a power of 2, can simplify formula to `C(n) = 2 C(n/2) + 2 n`.

```
    C(n) = 2 C(n/2) + 2 n
         = ( 2 C(n/2) + 2 (n/2) ) + 2 n
         = 2 ( 2 C(n/4) + 2 (n/2) ) + 2n
         = 2 ( 2 ( 2 C(n/8) + 2 (n/4) ) + 2 (n/2) ) + 2n
         = ...
         = 2^p C(n/(2p)) + 2 p n
         = n C(1) + 2 p n
         = 2 n lg(n)
```

(**Note:** `lg` means is log base 2.)

### Running Time

Although mergesort obviously has a lower asymptotic growth than insertionsort, for low `n` insertionsort is actually faster since it has a smaller constant cost in front of the `n`'s in the foruma.

Can use big Oh notation to indicate speed at high `n`.