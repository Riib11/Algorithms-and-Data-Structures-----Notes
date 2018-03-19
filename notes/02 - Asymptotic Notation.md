# Asymptotic Analysis

Here are some things I want to say:

```
    2 n lg(n) = O(d3 n^2 + d2 n + d1)
    d3 n^2 + d2 n + d1 != O(2 n lg(g))
    d3 n^2 + d2 n + d1 = Θ(n^2)             // big theta
    2 n lg(n) = o(d3 n^2 + d2 n + d1)       // little oh
```

**Def.** We say that `f(n) = O(g(n))` whenever there exists `c,m > 0` such that `0 ≤ f(n) ≤ c g(n)` for all `n ≥ m` (ignores constant factors).

**Prop.** `10 n^2 = O(n^3/4 - 20 n)`.

**Proof.** Note that `10 n^2 ≥ 0` for `n ≥ 0`. Let `n ≥ 20`. furthermore, consider `n^2 - 80`. Then `(n-2) n > 0` and `n^2 - n = (n-2) n + n > 80.` Now consider `40 (n^3/4 - 20 n) = 10 n (n^2 - 80) ≥ 10 n^2`. That means that `0 ≤ 10 n^2 ≤ 40 (n^3 - 20 n)`. So with choices `m = 80, c = 40` we can conclude that `10 n^2 = 0(n^3/4 - 20 n)` by definition of `O`.

**Prop.** If `f` is asymptotically non-negative, then `f(n) = O(c.f(n))` for any `c > 0`.

**Prop.** If `f,g` are asymptoically non-negative, then `f(n) + g(n) = O(max(f(n),g(n)))`.

**Proof.** Suppose `f,g` are asymptotically non-negative. Let `m1,m2` be constant. Let `m = max(m1,m2)`. Note that for `n ≥ m` we have `0 ≤ f(n) ≤ max(f(n),g(n))`. Similarly `0 ≤ g(n) ≤ max(f(n),g(n))`. Summing these we obtain that `0 ≤ f(n) + g(n) ≤ 2 max(f(n),g(n))` by choosing `m := max(m1,m2), c := 2`.

**Def.** We say that `f(n) = o(g(n))` whenever for any `c > 0` there exists an `m > 0` such that `0 ≤ f(n) ≤ c g(n)` for all `n ≥ m`.

**Claim.** `10 n^2 = o(n^3/4 - 20 n)`

**Proof.** Let `c > 0`. Let's consider `n^2 - (40/c) n - 80`. Using quad. form. an say
```
    (n - (20/c) - r) (n - (20/c) + r)
```
for `r = sqrt( (20/c)^2 + 80 )`. Let `n ≥ (20/c) + r`. This means that
```
    n^2 - (40/c) n - 80 ≥ 0
    => (c n^3 / 4) - 10 n^2 - 20 c n ≥ 0
    => 0 ≤ 10 n^2 ≤ c (n^3/4 - 20 n)
```
Therefor `10 n^2 = o(n^3/4 - 20 n)`.

**Theorem.** Let `f,g` be asymptotically positif. Then 
```
    lim_{n->∞}(f(n)/g(n)) = 0
    => f(n) = o(g(n))
```

**L'Hopital's Rule.** Let `f,g : R -> R` be differentiable over `[m,∞)` for the same `m in R`. Then
```
    lim_{n->∞}(f(n)) = lim_{n->∞}(g(n)) = ∞ => lim_{n->∞}(f(n)/g(n)) = lim_{n->∞}(f'(n)/g'(n))
```

**Def.** We say that `f(n) = Θ(g(n))` whenever there exists `c1, c2, m > 0` such that `0 ≤ c1 g(n) ≤ f(n) ≤ c2 g(n)` for all `n ≥ m`.

**Theorem.** If `f,g` are asymptotically positif and `lim_{n->∞}(f(n)/g(n)) = c > 0` then `f(n) = Θ(g(n))`.

**Claim.** `choose(n,2) = n(n-1)/2 = Θ(n^2)`.

**Proof.** We know that `n(n-1)/2 = (1/2) (n^2 - n) ≤ (1/2) n^2`. Let `n ≥ 2`. Thus `n^2 - 2n = n (n-2) ≥ 0` and so `(1/4) n^2 - (1/2) n ≥ 0` then //TODO//

**Claim.** `log_{b}(n) = Θ(lg(n))`.

**Proof.** `log_{b}(n) = log_{a}(n)/log_{a}(b) = lg(n)/lg(b)`. Let `k = log_{b}(n)` i.e. `b^k = n`. Then
```
lg(b^k) = lg(n)
=> k lg(b) = lg(n)
=>       k = log_{b}(n)
           = lg(n)/lg(b)
```