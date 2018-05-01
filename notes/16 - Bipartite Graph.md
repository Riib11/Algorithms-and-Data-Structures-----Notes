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

**Psuedocode:**

`ε` is the empty path.

    Alt-Match-BFS(U, V, E, M) :=
        
        # initialize to manage search
        for x in U union V
            x.mark := false
            x.pred := nil
            x.match := nil
        for (u,v) in M
            match := v
            v.match := u

        L := {} # list of nodes on the left
        for u in U
            if u.match = nil
                L := L union {u}

        # make alternating path, in a left-to-right search
        while L != {}
            R := {} # list of nodes on the right
            for u in L
                u.mark := true
                for v in V such that (u,v) in E
                    
                    # success! we are done
                    if v.match = nil
                        return Path-TO(v)
                    
                    # not done, so mark this node
                    # and add to R
                    else
                        v.pred := u
                        v.mark := true
                        R := R union {v}


            # right-to-left "extension"
            # builds next left layer, from R
            L := {}
            for v in R
                u := v.match
                if not v.mark
                    u.pred := v
                    L := L union {u}

    Path-To(x):
        if x.pred = nil
            return ε
        else
            reuturn Path-To(x.pred) • (x.pred, x)

Or can do

    Alt-Path-DFS(U, V, E, M) :=
        # same init as above, but without .pred
        for u in U
            if u.match = nil
                p := Alt-Path-Search-Right(u, ε, E)
                if p != nil
                    return p
        return nil

    Alt-Path-Search-Right(u, p, E) :=
        if u.mark
            return nil
        u.mark := true
        for v in V such that (u,v) in E
            p' := Alt-Path-Extend-Left(v, p • (u,v), E)
            if p' != nil
                return p'
        return nil

    Alt-Path-Extend-Left(v, p, E) :=
        if v.mark
            return nil
        if v.matched = nil
            return 'the path'
        u := v.match
        return Alt-Path-Search-Right(u, p • (v,u), E)