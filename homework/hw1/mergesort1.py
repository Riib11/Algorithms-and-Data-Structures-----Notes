from math import *

def mergesort (A):
    B = [ a for a in A ]
    return helper (A, B, 0, len(A))

def helper (A, B, start, finish):
    inversions = 0
    if finish-start > 1:
        middle = start + floor( (finish-start)/2 )
        inversions += helper (A, B, start, middle)
        inversions += helper (A, B, middle, finish)
        inversions += merge  (A, B, start, middle, finish)

    copyback (B, A)
    return inversions
    

def merge (A, B, start, middle, finish):    
    pointers = { "left": start, "right": middle }
    inversions = 0

    # fill in next A index with a pointer's target
    # increments pointer
    def put_next (p, i):
        B[i] = A[pointers[p]]
        pointers[p] += 1

    # fill in section of B
    for i in range (start, finish):
        left, right = pointers["left"], pointers["right"]

        if (left >= middle):
            next = "right"
        elif (right >= finish):
            next = "left"
        elif (A[left] >= A[right]):
            next = "right"
            inversions += 1
        else:
            next = "left"

        put_next (next, i)

    copyback (B, A)
    return inversions


def copyback (B, A):
    for i in range(len(B)): A[i] = B[i]


A = [1,2,3,4]

print("input",A)
inversions = mergesort(A)
print("output:",A)
print("inversions:",inversions)