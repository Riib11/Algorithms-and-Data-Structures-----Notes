from mergesort2 import mergesort
import random
from copy import deepcopy
random.seed()

# main

def main():

    # inputs
    test_count      = 30
    test_lengths    = [ random.randint(2,10) for _ in range(test_count) ]
    test_inputs     = [ makePermutation(l) for l in test_lengths ]

    # outputs
    test_outputs    = deepcopy (test_inputs)
    for ls in test_outputs: mergesort (ls)

    # log
    print("----------------------------------------------------------------------")
    print("| Sorted? | input -> output")
    print("----------------------------------------------------------------------")
    for i in range (test_count):
        print ("| ",checkSorted(test_outputs[i]),"  |", # success?
            test_inputs[i],"->",test_outputs[i]) # log
    print("----------------------------------------------------------------------")

# utility functions

def makeList (l):
    return [ i for i in range(l) ]

def makePermutation (l):
    ls = makeList(l)
    random.shuffle(ls)
    return ls

def checkSorted (ls):
    for i in range(len(ls)-1):
        if ls[i] > ls[i+1]: return False
    return True

# run

main()