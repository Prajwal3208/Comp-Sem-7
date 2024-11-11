import random
import time

# Deterministic Quick Sort
def deterministic_partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def deterministic_quick_sort(arr, low, high):
    if low < high:
        pi = deterministic_partition(arr, low, high)
        deterministic_quick_sort(arr, low, pi - 1)
        deterministic_quick_sort(arr, pi + 1, high)

# Randomized Quick Sort
def randomized_partition(arr, low, high):
    rand_index = random.randint(low, high)
    arr[high], arr[rand_index] = arr[rand_index], arr[high]
    return deterministic_partition(arr, low, high)

def randomized_quick_sort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quick_sort(arr, low, pi - 1)
        randomized_quick_sort(arr, pi + 1, high)

# Utility function to analyze both algorithms
def analyze_quick_sorts(arr):
    arr_copy = arr.copy()

    # Deterministic Quick Sort
    start = time.time()
    deterministic_quick_sort(arr, 0, len(arr) - 1)
    end = time.time()
    print(f"Deterministic Quick Sort Time: {end - start} seconds")

    # Randomized Quick Sort
    start = time.time()
    randomized_quick_sort(arr_copy, 0, len(arr_copy) - 1)
    end = time.time()
    print(f"Randomized Quick Sort Time: {end - start} seconds")

# Sample array for sorting
arr = [12, 4, 56, 17, 8, 99, 34, 23, 75, 3, 15]
analyze_quick_sorts(arr)
print("Sorted array (Deterministic):",arr)

# Deterministic Quick Sort Time: 2.2172927856445312e-05 seconds
# Randomized Quick Sort Time: 3.838539123535156e-05 seconds
# Sorted array (Deterministic): [3, 4, 8, 12, 15, 17, 23, 34, 56, 75, 99]
# ====================================================================================================================

# What is the difference between deterministic and randomized Quick Sort?

# A: Deterministic Quick Sort always selects a fixed position (like the first or last element) as the pivot, while Randomized Quick Sort selects a random element as the pivot. This randomization helps prevent worst-case performance, making the randomized version more efficient on average for various inputs.
# Q: What is the purpose of the partition function in Quick Sort?

# A: The partition function organizes elements around a pivot such that all elements less than the pivot are on its left, and all elements greater are on its right. It returns the final position of the pivot, allowing Quick Sort to recursively sort the left and right subarrays around the pivot.
# Q: Explain the Elbow Method in K-Means clustering.

# A: In the Elbow Method, the inertia (sum of squared distances of each point to its cluster center) is plotted against different numbers of clusters. The "elbow" or point where the rate of decrease sharply slows down indicates the optimal number of clusters for K-Means.
# Q: What is the worst-case time complexity of deterministic Quick Sort, and how does the randomized version improve it?

# A: The worst-case time complexity of deterministic Quick Sort is 
# 𝑂
# (
# 𝑛
# 2
# )
# O(n 
# 2
#  ), which can occur if the pivot consistently results in unbalanced partitions. Randomized Quick Sort mitigates this by selecting a random pivot, reducing the likelihood of unbalanced partitions, thus improving the average case to 
# 𝑂
# (
# 𝑛
# log
# ⁡
# 𝑛
# )
# O(nlogn).
# Q: Why is it beneficial to analyze both deterministic and randomized Quick Sort algorithms?

# A: Analyzing both algorithms helps in understanding how different pivot selection strategies affect performance. Randomized Quick Sort provides a more consistent 
# 𝑂
# (
# 𝑛
# log
# ⁡
# 𝑛
# )
# O(nlogn) performance across diverse inputs, whereas deterministic Quick Sort may be faster in certain cases but can degrade to 
# 𝑂
# (
# 𝑛
# 2
# )
# O(n 
# 2
#  ) on specific, unbalanced data.
# Q: How can you measure the execution time of Quick Sort in Python?

# A: You can use the time module in Python to record the start and end times of sorting functions. By calculating the difference, you obtain the execution time, which can be used to compare the performance of deterministic and randomized Quick Sort.

# : What are some strategies to choose a good pivot in Quick Sort?

# A:
# Median-of-three: Choose the median of the first, middle, and last elements as the pivot.
# Randomized selection: Randomly select a pivot to avoid patterns that lead to worst-case performance.
# Partitioning around the median: Select the median of the array as the pivot, although this can be costly to compute.

# What is the role of n_init in the K-Means implementation?

# A: The parameter n_init specifies the number of times the K-Means algorithm will be run with different centroid seeds. The final result is the best output from these runs, determined by the lowest inertia. This helps mitigate the effects of poor initial centroid placement.
# Q: Can you explain what inertia is in the context of K-Means clustering?

# A: Inertia measures how tightly the clusters are packed. It is calculated as the sum of the squared distances between each point and its assigned cluster centroid. Lower inertia indicates better clustering performance, as it suggests that the points are closer to their centroids.

# How does Quick Sort compare to Merge Sort in terms of time and space complexity?

# A: Quick Sort has an average and best-case time complexity of 
# 𝑂
# (
# 𝑛
# log
# ⁡
# 𝑛
# )
# O(nlogn) and a worst-case of 
# 𝑂
# (
# 𝑛
# 2
# )
# O(n 
# 2
#  ), while Merge Sort consistently performs at 
# 𝑂
# (
# 𝑛
# log
# ⁡
# 𝑛
# )
# O(nlogn) but requires 
# 𝑂
# (
# 𝑛
# )
# O(n) additional space for the temporary arrays used during merging. Quick Sort, being in-place, typically has better space efficiency.

# The term pivot generally means a central point, axis, or element around which something rotates or balances.
# A **pivot** is a specific element chosen from an array during the sorting process, particularly in algorithms like Quick Sort. It is used to partition the array into two sections: elements less than the pivot and elements greater than the pivot. The goal is to rearrange the array so that, after partitioning, the pivot is in its correct sorted position, allowing the algorithm to sort the subarrays on either side of it recursively.

