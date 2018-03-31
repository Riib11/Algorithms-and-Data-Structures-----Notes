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

So, need some operations: `zig, zag, zig-zig, zag-zag, zig-zag, zag-zig`.

Examples:

![](assets/images/splay02.png)
![](assets/images/splay03.png)

### Cool Properties

Sleator and Tarjan prove a series of "self-adjusts well" properties of a series of `m` accesses to a splay tree of size `n`.

**Theorem.** The total access tiems is `O((m+n) lg n + m)`

**Corralary.** If `m ≥ n` then `O(m(lg n + 1))` which is essencially `lg n` time _per access_.

**Proof Tech.** Developed analysis methods of _amortized performance_. _Potential method_ - change of potential:

    Φ(T) := "potential" for work of tree T

**Theorem.** (Static Optimality) Total access time is `O(m + sum([ q(i) lg(m/q(i)) for i=1..n ]))`

**Theorem.** (Working set) Let `t(j)` be the number of distinct items accessed since the last access to item at time `j`. Then the total access times is `O(m lg n + m + sum([ lg(t(j) + 1) for j=1..m ]))`. TL;DR: its as if for the working set, there is a balanced BST at the top of the splay tree.