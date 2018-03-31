# Bipartite Graph

A bipartite graph is constructed as

    G = (U, V, E) where
        U,V : Set Vertex
        E ⊆ (U, V) : Set Edge

**Degree:**
    
    deg(v) = # of edges incident to v

**Matchings:**

    M ⊆ E where
        (no vertex participartes in mode than one edge of M)
        forall v in V, deg_m(v) ≤ 1

**Cardinality:** Number of edges in a matching.

Standard algorithm relies on an augmenting step... candidate `M` find and **alternating path** `P` with respect to `M`.

**Alternating Path:** From some an uncovered `u` to some uncovered `v` is one with `def_M(u) = deg_M(v) = 0`, like

    u -- * ~~ * -- * ~~ ... -- * -- v

    Legend
        -- : excluded
        ~~ : included

    Compute:
        p  := Alternating-Path(G, M)
        M' := M ⊕ P
        ( i.e. flip incl/excl of edges in P to create matching M' )