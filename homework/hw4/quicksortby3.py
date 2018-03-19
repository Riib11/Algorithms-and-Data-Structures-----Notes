import random
random.seed()

def quicksortBy3(A, l, r):
    if l < r:
        i, j = partition(A, l, r)
        quicksortBy3(A, l, i-1)
        quicksortBy3(A, i+1, j-1)
        quicksortBy3(A, j+1, r)
    return A
    
def partition(A,l,r):
    x1 = l    # pivot 1 (choose leftmost)
    x2 = r    # pivot 2 (choose rightmost)
    p1 = l+1  # pointer 1
    p2 = x2-1 # pointer 2
    i  = l    # index
    
    # make sure that pivots are in order
    if A[x1] > A[x2]:
        swap(A,x1,x2)
        print(A)
    
    while p1 <= p2: 

        # less than first pivot
        if A[i] < A[x1]:
            swap(A,i,p1)
            i  += 1
            p1 += 1
            print(A)

        # greater than second pivot
        elif A[i] > A[x2]:
            swap(A,i,p2)
            p2 -= 1
            print(A)
        
        # between pivots
        else:
            i += 1

    p1 -= 1
    p2 += 1
    
    swap(A,p1,x1)
    print(A)
    
    swap(A,p2,x2)
    print(A)

    return p1, p2

def swap(A,i,j):
    A[i], A[j] = A[j], A[i]

A = [5,3,2,6,1,4]
print(A)
print(quicksortBy3(A,0,len(A)-1))