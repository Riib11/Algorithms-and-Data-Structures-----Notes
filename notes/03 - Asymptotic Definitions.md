# Asymptotic Definitions

## o(n): little oh

(Lower asymptotic order than.)

`f(n) = o( g(n) )` means that for all `c > 0`, there exists some `k > 0` such that, for all `n ≥ k`,
    
    0 ≤ f(n) ≤ c g(n).

## O(n): big Oh

(Asymptotic upper bound, ignore constant factors)

`f(n) = O( g(n) )` means there are positive constants `c,k` such that, for all `n ≥ k`,
    
    0 ≤ f(n) ≤ c g(n).

## ω(n): little omega

`f(n) = ω( g(n) )` means that for any `c > 0`, there exists a constant `k`, such that, for all `n ≥ k`,

    0 ≤ c g(n) ≤ f(n).

## Θ(n): big Theta

(Asymptoticall tightly bound, same asymptotic order)

`f(n) = Θ( g(n) )` means that there are positive constants `c1,c2,k` such that, for all `n ≥ k`,

    0 ≤ c1 g(n) ≤ f(n) ≤ c2 g(n).

## Asymptotically Non-Negative

`f(n)` is asymptotically non-negative if there exists `k > 0` such that for all `n ≥ k`, `f(n) ≥ 0`.