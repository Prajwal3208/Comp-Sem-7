import time

n = int(input("Enter the number of terms: "))

start_recursive = time.time()

# Recursive function to calculate the nth Fibonacci number
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Print the Fibonacci series using the recursive approach
print("Fibonacci series (recursive):")
for i in range(n):
    print(fibonacci_recursive(i), end=" ")

# Measure and display the execution time for the recursive approach
end_recursive = time.time()
print("\nRecursive Execution time is: {}ms".format((end_recursive - start_recursive) * 10**3))

# Measure the start time for the iterative approach
start_iterative = time.time()

# Iterative function to calculate the Fibonacci series up to n terms
def fibonacci_iterative(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

# Print the Fibonacci series using the iterative approach
print("Fibonacci series (iterative):")
print(" ".join(map(str, fibonacci_iterative(n))))

# Measure and display the execution time for the iterative approach
end_iterative = time.time()
print("Iterative Execution time is: {}ms".format((end_iterative - start_iterative) * 10**3))



"""
The recursive approach uses a function that repeatedly calls itself to calculate the Fibonacci number for a given position, leading to a high time complexity (O(2^n)) due to repeated calculations and a large call stack for each term. As a result, while it correctly outputs the series, it takes a significant amount of time to process even 30 terms (approximately 586 milliseconds).

On the other hand, the iterative approach efficiently calculates the series using a loop that tracks the last two numbers at each step. This approach has a linear time complexity (O(n)) and constant space complexity, making it far faster, as seen in the negligible execution time of around 0.4 milliseconds.
"""
# In the Fibonacci sequence, starting from 0 and 1, each number is the sum of the two previous ones:

# Example:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

# Here:

# 0 + 1 = 1
# 1 + 1 = 2
# 1 + 2 = 3
# 2 + 3 = 5, and so on.


# What is the time complexity of calculating Fibonacci numbers recursively?

# The time complexity is 
# 𝑂
# (
# 2
# 𝑛
# )
# O(2 
# n
#  ) due to the repeated calculations in each recursive call.
# Why is the non-recursive version of Fibonacci more efficient than the recursive one?

# The non-recursive version has a linear time complexity 
# 𝑂
# (
# 𝑛
# )
# O(n), avoiding redundant calculations present in the recursive approach.
# Explain the purpose of dynamic programming in calculating Fibonacci numbers.

# Dynamic programming stores previously calculated Fibonacci values to avoid redundant calculations, reducing time complexity to 
# 𝑂
# (
# 𝑛
# )
# O(n).

# What is memoization? How does it help in recursive Fibonacci calculations?

# Memoization is a technique of storing the results of expensive function calls to reuse them, reducing redundant calculations and improving efficiency.
# What is the role of base cases in the recursive Fibonacci function?

# Base cases (for 
# 𝑛
# =
# 0
# n=0 and 
# 𝑛
# =
# 1
# n=1) prevent the function from calling itself indefinitely and provide a stopping condition for recursion.
# How would you modify the recursive Fibonacci function to make it more efficient?

# By using memoization to store and reuse results of previous calculations, converting it to an 
# 𝑂
# (
# 𝑛
# )
# O(n) time complexity.
# What is the space complexity of the iterative Fibonacci function?

# The space complexity is 
# 𝑂
# (
# 1
# )
# O(1) as it only uses a fixed amount of memory for temporary variables.
# In what scenario is using recursion beneficial for calculating Fibonacci?

# Recursion might be more readable for educational purposes or very small values of 
# 𝑛
# n, but it’s not optimal for large 
# 𝑛
# n.

# Recursive: A recursive approach calculates Fibonacci numbers by calling the function within itself, breaking the problem into smaller subproblems (e.g., f(n) = f(n-1) + f(n-2)), but it can be inefficient due to repeated calculations for larger 
# 𝑛
# n.

# Non-Recursive: A non-recursive (iterative) approach uses a loop to calculate Fibonacci numbers, maintaining a few variables to track the last two numbers, making it more efficient and straightforward with linear time complexity.

# Which is Better: The non-recursive approach is generally better for larger 
# 𝑛
# n due to its linear time complexity and reduced overhead, while recursion can be more intuitive and easier to understand for smaller values.
    
    
