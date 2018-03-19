# Hash Table / Unordered Dictionary

- Set of distinct items
- (Key -> Value) mapping/store

Let `D` be an unordered dictinary. Then there are
    
    D.insert(k,v)    // add an entry to D with (k -> v)
    D.lookup(k) := v // get value associated with k
                     // v <- unfound if k not in D
    D.remove(k)      // remoev entry with key k

Keys are **primary:** distinct, identifying items.

Can implement with binary search tree, but this restricts to `Θ(lg n)` per operation.

Assume keys are drawn from a universe `U`. Use an array (table) of fixed size `m`. Assume some number of items `n`.

Typically, `n` will be around `m`, but `|U| >> m`!

**Goal:** Store `(k,v)` pairs directly in an array `T` and use constance-time access (property of arrays.)

**Idea:** Need a map that tells us where a key is stored in `T`.

**Hash Function:**
    
    h : U -> {0, 1, 2, ..., m-1}

Index `h(k)` where `k` will be located in `T`.

**Problem:** Can be collisions! Where

    h(k1) = h(k2), but k1 != k2

So, need a collision resolution strategy. And, try to avoid creating collisions.

**Example:** Suppose `U = Z`. Then choose `m` to be prime, and then let `h(k) := k mod m`.

##Bucket/Chain Hashing

Suppose `U = Σ*` for some finite alphabet `Σ` including a character `0`, where `Σ*` us all strings of characters within that alphabet, `|Σ| = D`. Assume keys `x = c.0 c.1 ... c.(l-1), 0`. Treat the characters of the string as digits from least to most significant in left-to-right order. Then

    code(x) := sum([ c.i D^i mod m ])

And finally,

    h(x) := code(x) mod m

This is a widely used and very effective hash. When things collide, add to linked-list at address: a **bucket/chain**:
    
    T.insert(k, v):      // inserts at front
        i := h(k)        // index from hash
        z := new node    // init new linked list node
        z.key   := k
        z.value := v
        z.next  := T[i]
        T[i]    := z     // add to bucket

    T.remove(k):
        i := h(k)
        z := T[i] // leader
        p := nil  // follower
        
        // find key's node
        while z.key != k
            p = z
            z = z.next
        
        // key was head
        if p == nil 
            T[i] = z.next
        
        // not at head
        else        
            p.next = z.next

`T.insert` assumes that `k in T`.

    T.lookup(k):
        i := h(k)
        z := T[i] // fist node in list
        while z != nil
            if z.key == k
                return z.value
            z := z.next
        return NOT_FOUND

#### Running times
    
    insert: (time to compute h) + Θ(1)
    lookup: (time to compute h) + {
        unsuccessful -> Θ(1 + α)
        successful   -> Θ(1 + α/2 - 1/(2m))
    }

#### Probabilistic Model of construction and access

"Simple uniform hashing". Any key is equally likely to hash to any slot (0..m-1)

Imagined `n` keys have been inserted. A successful search, assume any of `n` keys is chosen with equally probability.

##### Time for lookup: Unsuccessful

    E(time for uns. search)
    = 1 + sum([ 1/m sum([ P(t'th ke yinserted hashes to slot i) for i=1..n ]) for i=0..m-1 ])
    = 1 + (1/m) sum([ sum([ 1/m for t=1..n]) for i=0..m-1 ])
    = 1 + n/m

this is the mean depth of the buckets, and defined as load factor **α = m/n**.

##### Time for lookup: Successful

    to same slot
    E(time for suc. search)
    // the inner sum is the expected number of keys inserted after k_t that hash 
    = 1 + sum([ 1/n for sum([ P( h(k_s == h(k_t)) ) for s=t+1..n ])  t=1..n ])
    = 1 + (1/n) sum([ sum([ 1/m for s=t+1..n ]) for t=1..n ])
    = 1 + 1/(n m) sum([ n-t for t=1..n ])
    = 1 + 1/(n m) sum([ n-t for t=1..n ])
    = 1 + 1/(n m) n(n-1)/2
    = 1 + n/m - 1/(2m)
    = 1 + α/2 - 1/(2m)

## Open Addressing

Store key/values directly in hash table, where

    T[i] = either
        some key/value,
        unoccupied

So functions are

    T.insert(k)
        i := h.0(h)
        t := 0
        while t < m 
            if T[i] is unoccupied
                T[i] := k
                return
            t := t + 1
            i := h.t(k)
        raise ERROR                 // full table!

    T.lookup(k)
        i := h.0(k)
        t := 0
        while t < m
            if T[i] = m
                return FOUND
            if T[i] is unoccupied
                return NOT-FOUND
            t := t + 1
            t := h.t(k)

**Example**

## Linear Probing

Lets insert: `13, g, 8, 6, 60, 51, 93`. Build `T[0..6]` use "division method". Use

    h(k) := k mod 7

---
| 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| 6 | 8 | g | 51| 60| 93| 13|

go to the next avaliable to the right if the hash is occupied, and this keeps going until empty space or no spaces left to check. This is linear probing with stride `σ = 1`. But this leads to clustering, since spaces to the right of spaces that are occupied have a higher chance of being mapped to. Change stride could help? Maybe.

    h.t(k) := ( h(k) + t σ )

## Quadratic Probing

Choose `c1,c2` in

    h.t(k) := ( h(k) + c1 t + c2 t^2 ) mod m

Be careful when choosing `c1,c2`! e.g. `c1=0, c2=1` will not allow whole table to be accessed. But this leads to "secondary clustering"

## Double Hashing

Idea: choose some `h(k), h'(k)` and define

    h.t(k) := ( h(k) + t h'(k) ) mod m

Standard is to choose

    h (k) := k mod m
    h'(k) := 1 + (k mod m') != 0

and define for `m' < m` and relatively prime to `m`.