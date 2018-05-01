# Dynamic Programming

- 'Dynamic' means some applicatiosn relate to scheduling over time
- Devise a recurrence; usually exponential
- Solve the recurrence by filling out a (poly-size) table

### Application: Strings

Consider two strings `x,y in Σ*` where `Σ*` is the set of all strings of all lengths in alphabet `Σ`, including the empty string (σ).

    n := |x|
    σ.1 ... σ.n := x
    m := |y|
    τ.1 ... τ.m  := y

**Goal:** Find the longest common subsequence `z := LCS(x,y)`.

(Example of a subsequence: **A**G**GT**C**A**G -> AGTA)

Choose `l ≤ min(n,m)` where `i.i < i.(i+1)` and `j.i < j.(i+1)` such that `σ.(i.i) = τ.(j.i)`. Suppose `x' = x • σ, y' = y • τ, z' = LCS(x',y')`, and `z' = z • ρ`.

Two cases:

1. `σ = τ` => `ρ = σ = τ` and `z = LCS(x,y)`.
2. `σ != τ` =>
    1. `ρ != σ => z' = LCS(x, y • τ = y')`.
    2. `ρ != τ => z' = LCS(x • σ = x, y)`.

Base cases:

1. `LCS(ε, y) := ε`.
2. `LCS(x, ε) := ε`.
3. `LCS(x • σ, y • τ)` :=
    1. `σ = τ => LCS(x,y) • σ`.
    2. `σ != τ` => Longer of `{ LCS(x • σ, y), LCS(x, y • τ) }`

**Recurrence:**

    LCS(x • σ, y • τ) := {
        σ = τ =>
            LCS(x,y) • σ
        σ != τ =>
            Longest( LCS(x•σ,y), LCS(x,y•τ) )
    }

But we don't want to have evaluate this recursively.

**The Table Entries**

Define for all `i,j` wiht `0 ≤ i ≤ n`, `0 ≤ j ≤ n`,

    c[i,j] := | LCS( σ.1 σ.2 ... σ.i, τ.1 τ.2 ... τ.j ) |


Note that

    c[0,j] = c[i,0] = 0
    c[i,j] = {
        σ.i = τ.i => c[i-1,j-1]
        max{ c[i,-1j], c[i-1,j] } => σ.i != σ.j
    }

    d[i,0] = d[0,j] = (*)
    d[i,j] = {
        σ.i = τ.i => up-left
        σ.i != τ.i => max{ left entry, up entry } }

where `(*)` means "stop".

**The Table**

Example for `LCS("ACGCTAC", "CTGACA")`,

|     |**0**|**C**|**T**|**G**|**A**|**C**|**A**|
|-----|-----|-----|-----|-----|-----|-----|-----|
|**0**|  0  |  0  |  0  |  0  |  0  |  0  |  0  |
|**A**|  0  |  0  |  0  |  0  |  1  |  1  |  1  |
|**C**|  0  |  1  |  1  |  1  |  1  |  2  |  2  |
|**G**|  0  |  1  |  1  |  2  |  2  |  2  |  2  |
|**C**|  0  |  1  |  1  |  2  |  2  |  3  |  3  |
|**T**|  0  |  1  |  2  |  2  |  2  |  3  |  3  |
|**A**|  0  |  1  |  2  |  2  |  3  |  3  |  4  |
|**C**|  0  |  1  |  2  |  2  |  3  |  4  |  4  |

    Best-LCS(x,y) :=
        n := |x|
        m := |y|
        c := (n+1) by (m+1) table of 0
        d := (n+1) by (m+1) table of (*)
        for j from 1 to m
            if x[i] = y[j]
                c[i,j] := c[i-1,j-1] + 1
                d[i,j] := up-left entry
            else if c[i,j-1] > c[i-1,j]
                c[i,j] := c[i,j-1]
                d[i,j] := left entry
            else
                c[i,j] := c[i-1,j]
                d[i,j] := up entry

wysiwyg

**Running time**

    O(m n)

#### Example: Reading a book

Summer is 14 weeks long.
Some novel contains `N` sections, with lengths `l.1, l.2, ... l.N`.
`L.i = sum{ l.j for j from 1 to i }` is the number of pages after reading `i` sections.
`P = L.N`
`α = P/W`
`m.i = { "major section" => 1, "minor section" => 0 }`

**Goal**

Optimal schedule `1 = S.1 < S.2 < ... < S.W < S.(W+1) = N+1 (bogus)`
`S.k =` section # started on week `k`. Want to **minimize**

    sum{ (L.(S.k - 1) - L(S.k) - α)^2 + (1-m.(S.k)) β }

where `L.(S.k - 1) - L(S.k)` is the # of pages read in week `k` and `β` is some penalty factor.

    LP[k,i] := lowest penalty schedule for reading i sections in k weeks
    LP[k,i] := min{ LP[k-1,j] + L ... for j from 1 to i }