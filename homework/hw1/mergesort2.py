from math import *
from random import shuffle

def mergesort (A):
    
    # auxillary array
    B = [ a for a in A ]

    len_a = len(A)

    # sweeps with incrementally doubling sizes
    size = 1
    while size < len_a:

        # extra hanging off the end
        len_extra = len_a % (size*2)

        # sweep across A with (size*2)-steps
        for i in range (0, len_a-len_extra, size*2):
            merge (A, B, i, i+size, i+2*size)

        # update A
        copyback (B, A)

        # merge in extra (I'm guessing this isn't the optimal way)
        for i in range (len_a-len_extra, len_a):
            merge (A, B, 0, i, i+1)
            copyback (B, A)

        # increment size
        size *= 2


def merge (A, B, start, middle, finish):
        
    # pointers in left and right half of A
    pointers = { "left": start, "right": middle }

    # fill in next A index with a pointer's target
    # increments pointer
    def put_next (p, i):
        B[i] = A[pointers[p]]
        pointers[p] += 1

    # fill in section of B
    for i in range (start, finish):
        left, right = pointers["left"], pointers["right"]

        if   (left >= middle):      next = "right"
        elif (right >= finish):     next = "left"
        elif (A[left] >= A[right]): next = "right"
        else:                       next = "left"

        put_next (next, i)


def copyback (B, A):
    for i in range(len(B)): A[i] = B[i]
