# Radix Sort

First, understand count sort (in 08).

**Idea:** Universe is `{0..r^d - 1}`, and interpret keys of input array as base `r`. `d` is number of digits per entry, in base `r`.

    radixsort(A, n, r, d)
        // count array
        B := new array of [1..n]

        for p := 0 to d-1
            countsort by p'th digit, A -> B
            copy B back to A

**Example:**

    d = 3
    r = 10
    n = 9

    // does 3 passes over the 9 keys, and count sort one digit each time (left, middle, or right digit)
    // sort by 1's digit first, then r'2, then r^2's, etc.

    //    1st    2nd    3rd
    A =   ->     ->     -> 
    [ 961    310    310    162
    , 858    940    818    235
    , 310    961    235    310
    , 818    951    940    363
    , 940    162    951    818
    , 363    363    858    858
    , 951    235    961    940
    , 162    858    162    951
    , 235    818    363    961
    ]
