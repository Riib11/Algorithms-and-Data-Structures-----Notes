# Linear Time Sorting Algorithm

## Count Sort

Let `A` be an array of length `n` with indecies `0,...,n-1`, `A[i] in {0,...,m-1} for all i`. `{0,...,m-1}` is the _universe of keys_. `B` is the output.

idea: count the occurences of each key in [0,...,m-1]. Thne just fill in B with the amount at each i in [0,...,m-1]

    countsort(A, B, n, m)
        # store of counts
        count := new array index range [0..m-1], set to 0s
        # count occurences
        for i := 1 to n
            k := A[i]
            count[k] = count[k] + 1
        # prefix sum to determine placement
        for k := 1 to m-1
            count[k] = count[k] + count[k-1]
        # placement routing
        for i := n down to 1
            B[count[k]] = k
            count[k] = count[k] - 1

But this is bad for large universes. For example, if you are sorting integers (2^32-1 possible values), then you need something like a 4GB array to store the counts (assigning 8 bits to each entry).