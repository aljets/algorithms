# This algorithm takes an unsorted array as input and returns a sorted array in O(nlogn)

# Merge-Sort Algorithm
def merge_sort(numbers):
    global count
    n = len(numbers)
    if n < 2:
        return (numbers)
    #SPLIT into two, recurse
    left = merge_sort(numbers[:n/2])
    right = merge_sort(numbers[n/2:])
    i, j = 0, 0
    result = []
    #MERGE
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            count += len(left) - i
    result += left[i:]
    result += right[j:]
    return result

if __name__=="__main__":
    # Takes file as input with one integer entry per line
    file = open('integers.txt','r')
    lines = file.readlines()
    numbers = [int(e.strip()) for e in lines]
    file.close()

    count = 0
    answer = merge_sort(numbers)
print count # Returns the number of inversions
