import math
import random
import time

class Algorithm:
    DETERMINISTIC = 1
    RANDOMIZED = 2

# The partition function is used by both algorithms to partition the given array around a pivot element
def partition(array, start, end, pivot):
    for i in range(start, end):
        if array[i] == pivot:
            array[i], array[end] = array[end], array[i]
            break

    i = start
    for j in range(start, end):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1

    array[i], array[end] = array[end], array[i]
    return i

# Used in the deterministic approach to find the median of the given array
def findMedian(array, n):
    array.sort() # Sort the array
    return array[n // 2] # Return the middle element

# Function to find the k-th smallest element in the given array using the randomized approach
def kthSmallest(array, left, right, k, algorithm):
    if k > 0 and k <= right - left + 1:
        if algorithm == Algorithm.RANDOMIZED: # Randomized approach
            pivot = random.randint(left, right) # Choose a random pivot
            array[pivot], array[right] = array[right], array[pivot] # Swap the pivot with the last element
            pos = partition(array, left, right, array[right]) # Partition the array around the pivot
        else: # Deterministic approach
            n = right - left + 1 # Number of elements in the array
            median = [] # List to store the medians of all groups of 5 elements
            i = 0 

            while i < n // 5:
                # Find the median of the current group of 5 elements and add it to the list
                median.append(findMedian(array[left + i * 5: left + i * 5 + 5], 5))
                i += 1
            if i * 5 < n:
                # Find the median of the remaining elements
                median.append(findMedian(array[left + i * 5: left + i * 5 + n % 5], n % 5))
                i += 1
            if i == 1:
                # If there is only one group, the median of the group is the median of the array
                medOfMed = median[i - 1]
            else:
                # Otherwise, recursively find the median of the medians
                medOfMed = kthSmallest(median, 0, i - 1, i // 2, algorithm)

            # Partition the array around the median of the medians
            pos = partition(array, left, right, medOfMed)

        if pos - left == k - 1:
            return array[pos]

        if pos - left > k - 1:
            return kthSmallest(array, left, pos - 1, k, algorithm)

        return kthSmallest(array, pos + 1, right, k - pos + left - 1, algorithm)

    return math.inf

# Function to log the time taken to run a function in ms
def timeFunction(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    print("Time taken:", (end - start) * 1000, "ms")
    return result

def main():
    print("Random integers:")
    # An array of 1000 random integers
    array = random.sample(range(1, 10000), 9999)
    k = 15 # The k-th smallest element to find

    print("Deterministic:")
    timeFunction(kthSmallest, array.copy(), 0, len(array) - 1, k, Algorithm.DETERMINISTIC)

    # Find the k-th smallest element in the array using the randomized approach
    print("Randomized:")
    timeFunction(kthSmallest, array.copy(), 0, len(array) - 1, k, Algorithm.RANDOMIZED)

    print("\n\nSorted integers:")

    array.sort() # Sort the array

    print("Deterministic:")
    timeFunction(kthSmallest, array.copy(), 0, len(array) - 1, k, Algorithm.DETERMINISTIC)

    print("Randomized:")
    timeFunction(kthSmallest, array.copy(), 0, len(array) - 1, k, Algorithm.RANDOMIZED)

    # Reverse the array
    array.reverse()

    print("\n\nReversed integers:")
    print("Deterministic:")
    timeFunction(kthSmallest, array.copy(), 0, len(array) - 1, k, Algorithm.DETERMINISTIC)

    print("Randomized:")
    timeFunction(kthSmallest, array.copy(), 0, len(array) - 1, k, Algorithm.RANDOMIZED)


    
main()