# Ordered Dictionary

Keys are distinct.

## Implements:

    T.insert(k,v)
    T.lookup(k) := v
    T.delete(k)
    T.update(k,v')
    T.range_query(ki,kj)
        := { vi, ... , vj }
    T.inorder_traverse(p)     // maps p over T, in order
    T.predecessor(k)          // previous key, in order
    T.successor(k)            // next key, in order
    T.minimum()
    T.maximum()

## Implementation: Binary Search Tree

    BSTNode k v
        = Stub
        | Node
            { parent :: BSTNode
            , key    :: k
            , value  :: v
            , left   :: BSTNode
            , right  :: BS

    T.successor(x) := if x.right != nil
        then min_node(x.right)
        else first ancestor that it is the left of

    T.delete(k) := // assuming that k in T
        x := T.root
        while x.key != k
            if k < x.key
                then x := x.left
                else x := x.right
        T.excise_node(x)

    T.excise_node(x) :=
        p := x.parent
        match
            | x.left = nil  -> z := x.right
            | x.right = nil -> z := x.left
            | otherwise ->
                min_node_of_subtree(x.right) // move up
                T.excise_node(z)
        T.place_node(z,p)
