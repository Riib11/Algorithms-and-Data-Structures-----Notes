# Spanning Trees

**Spaning**: A subset `A` of `E` **spans** `G = (E,V)` when a subgraph `G_A = (V,A)` is connected.

**Spanning Tree**: A tree `T` subset of `E` is a **spanning tree** when `T` spans `G`.

Note: BFS, DFS, and Dijkstra's algorithm calculate spanning trees (not necessarily minimum spanning trees though).

## Spanning Tree Problem (MST)

    span(G) := { T subset E | T : spanning tree of G }

If `w : E -> Z` is the weight function on edges, then for `A subset E` define `w(A) := sum { w(e) | e in E }`.

### Problem Setup:

**Given:**
    
    G = (V,E)
    w : E -> Z

**Goal:**
    
    T in span(G) such that forall T' in span(G), w(T) ≤ w(T')

**Prim's-MST**(G, w)

    s := choose some element of G.V
    for v in G.V
        v.weight := ∞
        v.pred   := nil
    s.weight := 0
    H := new Min-Heap of G.V using .weight
    while H != {}
        u := H.remove-min() # lightest vertex connected to tree
        for v in G.V where (u,v) in G.E
            if v.weight > w(u,v)
                v.weight := w(u,v)
                v.pred   := u
                H.bubble-up(v)
    return { (v.pred, v) | v != s } # tree edges

**Claim:** `Prim's-MST(G, w)` is a minimum spanning tree.

To understand why this is true, check out some other more general structure of MSTs.

Let `W subset V`. This forms a cut `(W, V \ W)`. Then the **crossing edges** of this cut are `X(W) := { (u,v) in E | u in W, v in V \ W }`

**Respects a cut**: `A subset E` **respects a cut** if `A intersect X(w) = {}`.

**Light**: `X(w)` is **light** for a cut when `w(e) = min { w(e') | e' in X(w) }`.

**Find-MST**(G, w):

    F := {} # forest
    while |F| < |G.V| - 1 # while forest is not tree
        W := some cut that F respects
        e := light edge of X(w)
        F := F union {e}
    return F # will be tree

**Claim**: `Find-MST(G, w)` is a minimum spanning tree (easy to see). Then, `Prim's-MST` is an implementation of `Find-MST`, so the previous claim also follows.

**Theorem**: Let `F subset T` where `T` is a minimum spanning tree, `F` respect some cut `W`, and `e` be light for that cut. Then `F + e` is a subset of some MST.

**Proof**:

Suppose `e not in T`. Let `e in T intersect X(w)`. Consider `T' = (T = e') \ {e}`, which is also a spannng tree. Then

    w(T') = w(T) - w(e') + w(e)
    w(T') ≤ w(T) # since w(e) - w(e') ≤ 0

SO `T'` is also a minimum spanning tree.