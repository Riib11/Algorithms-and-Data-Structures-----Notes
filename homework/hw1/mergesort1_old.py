from math import *

def mergesort (A):
    B = [ a for a in A ]
    return helper (A, B, 0, len(A))

# counts inversions during mergesorting A[start:finish]
def helper (A, B, start, finish):

    inversions = 0    
    
    # not sorted
    if (start < finish):
        middle = ceil( (start+finish)/2 )
        inversions += helper (A, B, start, middle-1)
        inversions += helper (A, B, middle, finish)
        inversions += merge  (A, B, start, middle, finish)
        copyback (B, A)

    print(A)

    return inversions

# counts inversions during sorting merge
def merge (A, B, start, middle, finish):

    pointers = { "left": start, "right": middle }
    inversions = 0

    def put_next (p, i):
        B[i] = A[pointers[p]]
        pointers[p] += 1

    for i in range(start,finish):
        left, right = pointers["left"], pointers["right"]

        if (left >= middle): next = "right"
        elif (right >= finish): next = "left"
        elif (A[left] >= A[right]):
            next = "right"
            inversions += 1
        else: next = "left"

        put_next (next, i)

    return inversions

def copyback (B, A):
    for i in range(len(A)): A[i] = B[i]

A = [1,2,3,4]

print(A)
print(mergesort(A))
print(A)