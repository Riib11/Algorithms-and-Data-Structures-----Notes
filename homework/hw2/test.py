import math

f = lambda k: 2**(2**k)

def ls(x): return [ f(x) for x in range(x) ]

def prod(xs):
    product = 1
    for x in xs: product *= x
    return product

print(ls(5))
print([ prod(ls(x)) for x in range(5) ])