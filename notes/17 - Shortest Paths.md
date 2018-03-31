# Shortest Paths

## Single Source Shortest Path Problem with Positive Weights (SSSP+)

(Dijkstra's Algorithm : Textbook 24.3)

**Given:**
    
    G = (V, E), s in V, w : E -> Z+

**Define:** for any path `p` (sequence of edges)

    w(p) := sum([ w(e) for e in p ])

    distance:
    d(u,v) := min( ∞ ++ [ w(p) for u~p~>v ])


**Find:** `d(s,v)` for all `v in V`.

**Use:** Dijkstra's algorithm (requires positive weights) which computes `v.dist, v.pred`.

**Observation:**

* If `v != s` and `v.dist < ∞`, then for the shortest path `p = e.1, e.2, ... e.k`, `e.k = (v.pred v)`.

* If `v = s`, then `v.dist = 0`, `v.pred = nil`.

* If `v.dist = 0`, then `v.pred = nil`.

### Dijkstra's Algorithm

    Dijkstra's-SSSP+(G, s, w) :=                        # Run time:
        for v in G.V do                                 # n
            v.dist := ∞                                 # | n
            v.pred := nil                               # | n
        s.dist := 0                                     # 1
        H := build a heap with priorities v.dist        # n
        while H := {} do                                # n
            u := H.Remove-Min()                         # | lg n
            for v in { v in G.V | (u,v) in G.E } do     # | m
                if v.dist > u.dist + w(u,v) then        #   | 1
                    v.dist := u.dist + w(u,v)           #   | 1
                    v.pred := u                         #   | 1
                    H.Bubble-Up(v)                      #   | lg n

**Claim:** When `u` is chosen from `H` wiht minimum distance, `u.dist = d(s,u)`.
**Proof:** Suppose, for the sake of contradiction, `u.dist != d(s,u)` for at least some `u`'s. Consider the first time that a vertex `u` is removed from `H` where `u.dist != d(s,u)` (first time that induction hypothesis would break for positive claim). Because this is the first time, there is a shortest path `p` to `u.pred`, such that

    w(p) = u.pred.dist = d(s,u.pred)

So we have something like

    s ––p––> u.pred -> u
    |          Λ
    \––\       |
    p'  \–>u'–>v'

where `p'` is a shorter path than `p` and

    w(p') < w(p) + w(u.pred,u)

Consider vertices along `p'`, and let `(u',v')` cross into `H` (i.e. `u' not in H`, `v' in H`, `(u',v') in p'`) which is possible since `u != s ...`. Node that, since weights are positive:

    v'.dist ≤ u'.dist       # v' was seen when u' was visited
    + w(u',v') ≤ w(p')      # maybe there are more edges along p' but path is part of p'
    < w(p) + w(u.pred,u)    # already visited u.pred
    = u'.dist + w(u.pred,u) # already visited u.pred
    = u.dist
    => v'.dist ≤ u.dist
    => false! since then we would choose v' over u when Remove-Min
        def of u is the one that with mim dist that we remove next



## Bellman-Ford (SSSP)

(Bellman-Ford SSSP : Textbook 24.1)

Lets allow 0 and negative weight edges:

    w : E -> Z

Consider the case where there is a round from `s` to `v` that meanders through a negative weight cycle:

    s –––> p –––> v
          / \
         ↓   ↑ (net weight change is negative)
          \_/

Then `d(s,v) = -∞`.

**Simple Path:** a path with no loops = no repeated vertices.

**Claim:** Suppose that `-∞ < d(s,v) < ∞`. Then there's a shortest path that's simple.

**Observation:** A simple path can have at most `n-1` edges.

**Define:**

    D.l(s,v) = min { w(p) | s ~p~> v where |p| ≤ l }

**Observation:**

    D.0(s,v) = {
        v = s  => 0
        v != s => ∞
    }

**Observation:**

    D.1(s,v) = {
        v = s          => 0
        (s,v) in E     => w(s,v)
        (s,v) not in E => ∞
    }