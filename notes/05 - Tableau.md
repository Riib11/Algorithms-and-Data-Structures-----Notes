# Tableau

A array2D-like heap

## Young Tableau

A Tableau where each cell is greater than the cell above and the cell to the left of it.

Can have d-ary heaps rather than binary heaps too.

## Heap Sort

`A` is an array. Have `A[0..i-1]` be organized as a heap. Then We are trying to insert `A[i]`. This is easy using `trickle-down`. Then repeat this for the next element, and this is the sorting algorithm!

    heap_sort (A) := {
        
        n = |A|

        // build heap
        for i = n/2 down to 1 do
            trickle_down(A,n,i)
        
        // swap and fix heap
        for i = n do to 1 do
            swap(A,i,1)
            trickle_down(A,i-1,i)
    
    }

### Runtime analysis

`build heap` runs `n/2` times and `trick_down` is `O(lg n)`, so `build heap` is `(n/2) O(lg n) = ­Θ(n)`

`swap and fix heap` runs `n` times and so is `n O(lg n)`. Is `Θ(n lg n)` in "worst case".