# Algorithms - Homework 2

Henry Blanchette
Section 1
    
## 1.a

Given:

    R(n>1) := R(⌊n/2⌋) + n
    R(1)   := 1

Let `n = 2^p` for some large natural number `p`. Then

    R(n)
    = R(2^p)
    = R(2^(p-1)) + 2^p
    = R(2^(p-2)) + 2^(p-1) + 2^p
    = R(2^(p-p)) + ... + 2^(p-1) + 2^p
    = 1 + 2^1 + 2^2 + ... + 2^p
    = 2^0 + 2^1 + ... + 2^p
    = sum([ 2^k for k in [1..p] ])
    = (1 - 2^(p+1)) / (1 - 2)
    = 2^(p+1) - 1
    = 2 (2^p) - 1
    = 2 n - 1.

## 1.b

Given:

    Q(n>2) := Q(⌊sqrt(n)⌋) + 1
    Q(2)   := 1
    Q(1)   := 0

Let `n = 2^(2^p)` for some large natural number `p`. Then

    Q(n)
    = Q( 2^(2^p) )
    = Q( 2^(2^(p-1)) ) + 1
    = Q( 2^(2^(p-2)) ) + 1 + 1
    = Q( 2^(2^(p-p)) ) + 1 + ... + 1
    = Q(2) + p
    = 1 + p
    = 1 + lg(lg(n)).

## 1.c

Let `n = 2^(2^p)` for some large natural number `p`. Then

    P(n)
    = 2^(2^(p-1)) P(2^(2^p-1)) + 1
    = 2^(2^(p-1)) [ 2^(2^(p-2)) P(2^(2^p-2)) + 1 ] + 1
    = [ 2^(2^(p-1)) * ... * 2^(2^(p-p)) ] + [ 2^(2^p-1) + ... + 2^(2^p-p) ] + 1
    = 2^( 2^(p-1) + ... + 2^(p-p) ) + 2^2^(p(p-1)/2) + 1
    = 2^(2^p - 1) + 2^(2^(p(p-1)/2)) + 1
    = 2^(2^p - 1) + 2^(2^(p(p-1)/2)) + 1.

## 2

**Prop:** `lg(n!) = Θ( n lg(n) )`.

**Proof:** Let `n ≥ 1` be a multiple of 2, `c1 = 1/2`, and `c2 = 1`. Then

    lg(n!)
    = lg(1) + ... + lg(n/2) + lg(n/2 + 1) + ... + lg(n)
    ≥ 0     + ... + 0       + lg(n/2)     + ... + lg(n/2)
    = (n/2) lg(n/2)
    = (n/2) lg(n) + (n/2) lg(2)
    = (n/2) lg(n) + o( (n/2) lg(n) )

We can ignore the `o( (n/2) lg(n) )` it in the check for `Θ` (as proved in 4.c). So this yeilds

    -> (n/2) lg(n)
    = c1 n lg(n)

Additionally,

    lg(n!)
    = lg(1) + ... + lg(n)
    ≤ lg(n) + ... + lg(n)
    = n lg(n)
    = c2 n lg(n)

So `c1 lg(⌈n/2⌉) ≤ lg(n!) ≤ c2 lg(n) => lg(n!) = Θ( n lg(n) )`.

## 3 

**Prop:** `(lg(n))^(lg(n)) = Θ( n^(lg(lg(n))) )`.

**Proof:** Let `n = 2^(2^p)` for large `p`. Then
    
    lg(n)^lg(n)
    = lg(2^(2^p))^lg(2^(2^p))
    = (2^p)^(2^p)
    = 2^(p 2^p)
    = (2^(2^p))^p
    = (2^(2^p))^( lg(lg(2^(2^p))) )
    = n^( lg(lg(n)) )

Since for such and arbitrary large `p` these functions are equal, they should be asymptotically tightly bound, so `Θ` aptly describes their relationship.

## 4.a

**Prop:** Let `f(n) = O( g(n) )`, `lg(g(n)) ≥ 1` and `f(n) ≥ 1` for sufficiently large `n`. Then `lg(f(n)) = O( lg(g(n)) )`.

**Proof:** `f(n) = O( g(n) )` implies that for any `c > 0`, there exists `k` such that, for all `n ≥ k`, `0 ≤ f(n) ≤ c g(n)`. Additionally `f(n) ≥ 1 => lg(f(n)) ≥ 0`. Then

    1 ≤ f(n) ≤ c g(n)
    => 0 ≤ lg(f(n)) ≤ lg(c g(n))
    => 0 ≤ lg(f(n)) ≤ lg(g(n)) + lg(c)  // system I
    => 0 ≤ lg(f(n)) ≤ c' lg(g(n))       // system II

for `c' = 2` since `( lg(g(n)) + lg(c) ) / lg(g(n)) -> 1 ≤ 2 = c'` for large enougn `n`, which yields

    c' lg(g(n))
    ≥ ( ( lg(g(n)) + lg(c) ) / lg(g(n)) ) lg(g(n))
    = lg(g(n)) + lg(c),

justifying the step from system I to II. Since this `c'` exists, `lg(f(n)) = O( lg(g(n)) )`.

## 4.b

**Prop:** Let `f(n) = O( g(n) )`. Then `2^f(n) = O( 2^g(n) )`.

**Proof:** `f(n) = O( g(n) )` implies that for any `c > 0`, there exists `k` such that, for all `n ≥ k`, `0 ≤ f(n) ≤ c g(n)`. Then

         0 ≤ f(n)   ≤ c g(n)
    => 2^0 ≤ 2^f(n) ≤ 2^(c g(n))
    =>   1 ≤ 2^f(n) ≤ 2^c 2^g(n)
    =>   0 ≤ 2^f(n) ≤ c'  2^g(n)

Since `c' = 2^c` exists, `f(n) = O( g(n) )`.

## 4.c

**Prop:** Let `g(n) = o( f(n) )`. Then `f(n) + g(n) = Θ( f(n) )`.

**Proof:** `g(n) = o( f(n) )` implies that for all `c > 0`, there exists some `k > 0` such that for all `n ≥ k`, `0 ≤ g(n) ≤ c f(n)`. So there is such a `k` past which `c = 1/2` works. Then `f(n) ≤ 1/2 g(n)`. So,
    
    g(n) ≤ 1/2 f(n)
    => f(n) + g(n) ≤ 3/2 f(n)

and
    
    1/2 f(n) ≤ f(n)
    => 1/2 f(n) ≤ f(n) + g(n).

Since `c' = 1/2, c'' = 3/2` exist such that `c' f(n) ≤ f(n) + g(n) ≤ c'' f(n)` for all `n > k`, `f(n) + g(n) = Θ( f(n) )`.

## 5

Let `p(n) = sum([ a_i n^i for i in [0..d] ])`, where `a_i > 0` for all `i`.

## 5.a

**Prop:** `p(n)` is asymptotically non-negative.

**Proof:** Let `k = 0`. Then for all `n > k`, `n^i > 0`. Then, since `a_i > 0` for all `i`, each of `a_i n^i > 0`, so the sum of all of them is non-negative.

## 5.b

**Prop:** Let `k ≥ d`. Then `p(n) = O(n^k)`.

**Proof:** Let `l ≥ 0`. Then for all `n ≥ l`,

    p(n)
    = a_1 n^1 + ... + a_d n^d
    ≤ a_1 n^d + ... + a_d n^d
    = n^d(a_1 + ... + a_d)
    ≤ n^k(a_1 + ... + a_d)

Since `c = (a_1 + ... + a_d)` exists such that `p(n) ≤ c n^k` for all `n ≥ l` for all `l ≥ 0`, `p(n) = O(n^k)`.

## 5.c

**Prop:** Let `k > d`. Then `p(n) = o(n^l)`.

**Proof:** Let `c > 0` and `l` be the `(k-d)`th root of `(a_1 + ... + a_d) / c`. Then for `n ≥ l`,

               n ≥ l
    =>   n^(k-d) ≥ (a_1 + ... + a_d) / c
    => c n^(k-d) ≥ a_1 + ... + a_d
    =>     c n^k ≥ n^d a_1 + ... n_d + a_d)
    =>     c n^k ≥ n_1 a_1 + ... n_d + a_d
    =>     c n^k ≥ p(n)

Since `l` exists such that `c n^k ≥ p(n)` for all `n ≥ l`, `p(n) = o(n^k)`.

(Do you prefer this format, or LaTex?)