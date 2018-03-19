import random
random.seed()

def quicksort(A,l=0,r=False):
    r = r or len(A)-1
    if l < r:
        p = partition(A,r,l,r)
        quicksort(A, l,   p-1)
        quicksort(A, p+1, r)

def partition(A,p,l,r):
    # pivot
    pivot = A[p]
    # start i at left side
    i = l-1
    # sweep j left to right
    for j in range(l,r):
        if A[j] < pivot:
            i += 1
            print(A)
            print("i="+str(i),"j="+str(j),"p="+str(pivot))
            swap(A,i,j)
        else:
            print(A)
            print("i="+str(i),"j="+str(j),"p="+str(pivot))
    swap(A,i+1,r)
    print(A)
    print("end",l,r)
    return i+1

def swap(A,i,j):
    print("swapping:",i,j)
    A[i], A[j] = A[j], A[i]
    
A = [4,2,5,1,0,3]
quicksort(A)
print(A)