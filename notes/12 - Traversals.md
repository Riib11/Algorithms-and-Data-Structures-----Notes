# Traversals

This will act upon a BSTree, but generalizes to graph traversals.

## In Order

    T.inorder_traverse() :=
        x := T.min_node() // worst case: n
        while x := nil
            visit(x)
        x := succ_node(x) // can be complicated...
                          // worse case: n?

this would lead to `O(n^2)` time, but that's not the case. Actually, its `Θ(n)`, since you touch each node 3 times, and go along each edge twice, and both of these things are linear in `n`. So instead, can do it recursively:

    T.inorder_traverse() :=
        inorder(T.root)

    inorder(x) :=
        if x != nil
            inorder(x.left) // access each down link once (linear with n)
            visit(x)        // access each node once (linear with n)
            inorder(x.right) // access each down link once (linear with n)

    visit(x) :=
        print(x.key) or the like

So, is `Θ(n)`.

    preorder(x) :=
        if != nil
            visit(x)
            preorder(x.left)
            preorder(x.right)

This is good for recreating the tree (tear down then recreate). For example, could write contents of graph to an array in a file, and then load them back into a tree by doing a bunch of inserts.

What about `insert`, `delete` and `lookup`?
 
    worst case: linear time (if tree is completely unbalanced)
    typically:  log. of size of tree, Θ(lg n) (if average balance)