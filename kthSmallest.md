# K-th smallest algorithm

## Implementation

You can find an implementation of both algorithms in the file both.py. You can run the basic test case using:

```
python both.py
```

The 2 implementations share most of their code, the only difference being the way the array is partitioned: the random method chooses a random element to partition against, while the deterministic method uses finds the median of medians and partitions against that.

## Performance analysis

### Deterministic Method using the Median-of-Medians Algorithm

**Worst-case time complexity:** \(O(n)\)

We can prove the time complexity using induction. We start with the base case: for an array of size 5, the algorithm can find the median in constant time.

Induction:

Assume that the algorithm works in (O(n)) time for arrays of size (k), where (k < n). Now consider an array of size (n). We have the following steps:

1. Divide the array into groups of five elements. This takes (O(n)) time.
2. Find the median of each group. By the inductive hypothesis, this takes (O(n/5)) time for each group - (O(n)) total.
3. Find the median of the medians - (O(n/5)).
4. Partition the array around the median of medians - (O(n)).
5. Recursively find the desired element in the appropriate subarray. By the inductive hypothesis, (O(3n/4)) time in the worst case.

Therefore, the total time complexity is (O(n) + O(n) + O(n/5) + O(n) + O(3n/4)), which simplifies to (O(n)).

### Randomized Method using Randomized Quicksort

**Expected time complexity:** \(O(n)\)

We can prove this using the master theorem for recurrence relations. The recurrence relation for the expected time (T(n)) is:

```
T(n) = max{T(n/2), T(3n/4)} + O(n)
```

The first term accounts for the recursive calls on the subarrays, and the second term accounts for the partitioning and pivot selection.

Using the master theorem with (a = 1), (b = 2), and (c = 1), we find that (log_b(a) = 0) and (c = 1). Since (c > log_b(a)), the master theorem tells us that T(n) = O(n^{log b(a) + c} = O(n)).

This shows that the expected time complexity is O(n)

## Space Complexity & Overhead

**Deterministic:**

The deterministic method provides an optimal space complexity of O(N), used for storing the input array. In my implementation however, it also requires additional space for storing the medians of the groups and for the recursive calls. The space used for these overheads is, however, a fraction of the input size.

**Randomized:**

The randomized method also ideally requires O(n) for the input array. However, it has an added overhead for the recursive calls, even though again, it is typically small.

Both deterministic and randomized selection algorithms achieve (O(n)) time complexity, but with different guarantees. The deterministic algorithm provides a guaranteed worst-case bound, while the randomized algorithm provides an expected time bound. The space complexity and overheads for both algorithms are similar.

## Empirical Analysis

These are the results from running the sample case: (the array contains 9999 numbers, ranging from 1 to 10k)

```
Random integers:
Deterministic:
Time taken: 5.235195159912109 ms
Randomized:
Time taken: 2.1910667419433594 ms

Sorted integers:
Deterministic:
Time taken: 4.743814468383789 ms
Randomized:
Time taken: 1.585245132446289 ms

Reversed integers:
Deterministic:
Time taken: 4.901885986328125 ms
Randomized:
Time taken: 3.8118362426757812 ms
```

Based on the provided results, it is clear that the randomized method outperforms the deterministic method in all cases. There are numerous possible explanations for this, one of which is that my findMedian function uses the native .sort() funtion to sort the array and determine the median, which can come with a complexity of o(nlogn). An improvement there would be to use the k-th smallest method to determine the median if the array size is large, and fallback to a fast sorting algorithm when the array gets down to a manageable size, like 5.

This shows that while the theoretical analysis provides valuable understanding of algorithmic behaviour, it is essential to time algorithms in practical scenarios. There are many possible variables that are hard to detect and plan for, which might affect the real-world performance of algorithms.
