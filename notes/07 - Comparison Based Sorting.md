# Comparison Based Sorting

Examples: insertion, selection, bubble, merge, heap, quick

**Comparison Based:** For fixed input size `n`, its determination of reordering to sort that array is based entirely on answering questions of hte form "Is `A[i] ≤ A[j]`?" for positions `i,j in [1..n]`.

**Claim:** A comparison-based sorting algorithm uses at least `Ω(n lg n)` comparisons in its worst case.

**Proof** All comaprison-based sorting algorithms will result in a decision tree that ends in a particular permulation – one that permutes the original array into its ordered form.

**Claim:** For a binary tree, let the number of internal nodes be `N` and the number of leaves be `L`. Then

    N = L-1

Let `H` be the height of the tree. Then lets relate `H` to `N`;

    2^(H+1) - 1 = 1 + 2 + 4 + ... + 2^4 // full binary tree
                ≥ 2L - 1                // number of nodes

and so

    2^ ≥ L

which means that

    H ≥ lg L ≥ lg(n!)

THerefor sorting algorithm uses `Ω(n lg n)` comparisons in worst case.