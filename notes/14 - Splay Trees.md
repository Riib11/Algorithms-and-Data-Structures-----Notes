# Splay Trees

A variant of a BSTree with rotations to restructure. It doesn't contain any additional info in the tree, like height (AVL Trees) or colors (Red-Black Trees).

Inspired by "move to front" (MTF) hueristic for linked lists:

    lookup target in
    (head -> node -> node -> node -> node (target) -> ...)
    maps to
    (head -> node (target) -> node -> node -> node -> ...)

This heuristic is good in some "online", "competative" sense. Also, it doesn't make the operations on the list any worse than without MTF implemented.

### Splay Operation

![](assets/images/splay01.png)

Splay is a series of "double rotation" (and maybe one single rotation) that moves target node to root.

**Node:** A splay is not a series of (the obvious) rotations! (provably bad)