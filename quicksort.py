# This algorithm takes an unsorted array as input and returns a sorted array in O(nlogn)
# Below are two versions, one is a simple version and the other is an in-place version
# which uses less memory

import random

# Partition subroutine
def partition(list,p):
    # Place pivot as first element
    list[p], list[0] = list[0], list[p]
    j = 1
    # Advance along list, if element is less than pivot swap places
    # This places all elements less than pivot at a position less than
    # place j
    for i in range(1,len(list)):
        if list[i] <= list[0]:
            list[i], list[j] = list[j], list[i]
            j += 1
    list[0], list[j-1] = list[j-1], list[0]
    return (list,j)        

# Choose pivot subroutine
def choosepivot(list):
    #Compute pivot based on middle of three elements
    n = len(list)
    first = list[0]
    middle = list[int((n - 1)/2)]
    last = list[n - 1]
    if middle <= first <= last or last <= first <= middle:
        return 0
    if first <= middle <= last or last <= middle <= first:
        return int((n - 1)/2)
    if first <= last <= middle or middle <= last <= first:
        return n - 1

# Simple quick-sort
def quicksort(list):
    n = len(list)
    if n <= 1:
        return list
    # Choose a pivot
    p = choosepivot(list)
    # Elements in pivot
    elements = list[:p] + list[p+1:]
    # Partition array around pivot and recursively sort partitions
    a = quicksort([x for x in elements if x < list[p]])
    b = quicksort([x for x in elements if x >= list[p]])
    return a + [list[p]] + b

# In place quick-sort
def quicksort_in_place(list):
    global count
    n = len(list)
    if n <= 1:
        return list
    # Choose a pivot, partition, and return j location of pivot
    p = choosepivot(list)
    list,j = partition(list,p)
    # Recurse along these lists that are less than or greater than pivot
    a = quicksort_in_place(list[:j-1])
    b = quicksort_in_place(list[j:])
    count += len(a) + len(b)
    return a + [list[j-1]] + b        
        
if __name__=="__main__":
    # Takes file as input with one integer entry per line
    file = open('integers.txt','r')
    lines = file.readlines()
    numbers = [int(e.strip()) for e in lines]
    file.close()

    count = 0
    answer = quicksort_in_place(numbers)
    print count # Returns the number of inversions
