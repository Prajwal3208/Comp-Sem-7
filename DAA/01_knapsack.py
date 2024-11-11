def knapsack_01(n, values, weights, W):
    dp = [[0] * (W+1) for _ in range(n+1)]

    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    
    selected_items = []
    i, w = n, W
    while i > 0 and w > 0:
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1)
            w -= weights[i-1]
        i -= 1
    
    return dp[n][W], selected_items

if __name__ == "__main__":
    n = int(input("Enter the number of items: "))
    
    values = []
    weights = []
    
    for i in range(n):
        value = int(input(f"Enter the value of item {i+1}: "))
        weight = int(input(f"Enter the weight of item {i+1}: "))
        values.append(value)
        weights.append(weight)
    
    W = int(input("Enter the capacity of the knapsack: "))
    
    max_value, selected_items = knapsack_01(n, values, weights, W)
    
    print(f"Maximum value in knapsack: {max_value}")
    print("Selected items (indices):", selected_items)


# """Branch and Bound is an algorithmic technique used to solve optimization problems by exploring all possible solutions in a systematic way. In the context of sorting, it can be applied to problems where there are additional constraints, such as minimizing swaps or comparisons. The process involves branching into subproblems, bounding to evaluate the best possible solutions, and pruning to discard suboptimal paths. While not commonly used in traditional sorting algorithms, it can optimize constrained sorting tasks. It’s mainly used when sorting involves optimization beyond just arranging data in order."""

# Worst-case: O(2^n)
# Best-case: O(n×W) 
# def Knapsack_using_DP(profit,weight,capacity):
#     n=len(profit)
#     dp=[[0 for _ in range(capacity+1)] for _ in range(n+1)]
    
#     for i in range(n+1):
#         for w in range(capacity+1):
#             if w==0 or i==0:
#                 dp[i][w]=0
#             elif weight[i-1]<=w:
#                 dp[i][w]=max(profit[i-1]+dp[i-1][w-weight[i-1]],dp[i-1][w])
#             else:
#                 dp[i][w]=dp[i-1][w]
#     selected_items=[]
#     i,w=n,capacity
#     while i>0 and w>0:
#         if dp[i][w]!=dp[i-1][w]:
#             selected_items.append(i-1)
#             w=w-weight[i-1]
#         i=i-1
#     return dp[n][capacity],selected_items
    
# if __name__ == "__main__":
#     n=int(input("Enter the total no of objects: "))
#     profit=[]
#     weight=[]
#     for i in range(n):
#         ele=int(input(f"Enter the profit of {i+1}th object: "))
#         profit.append(ele)
#     for i in range(n):
#         ele=int(input(f"Enter the weight of {i+1}th object: "))
#         weight.append(ele)
#     capacity=int(input("Enter the capacity of the element: "))
#     ans,selected_items=Knapsack_using_DP(profit,weight,capacity)
#     print("The maximum profit is: ",ans)
#     for i in selected_items:
#         print(f'item: {i+1} and its weight: {weight[i]} and profit: {profit[i]}')


# Enter the total no of objects: 2
# Enter the profit of 1th object: 50
# Enter the profit of 2th object: 100
# Enter the weight of 1th object: 60
# Enter the weight of 2th object: 120
# Enter the capacity of the element: 500
# The maximum profit is:  150
# item: 2 and its weight: 120 and profit: 100
# item: 1 and its weight: 60 and profit: 50


# ====================================================================================================================

# What is the 0-1 Knapsack Problem?

# The 0-1 Knapsack Problem is a combinatorial optimization problem where, given a set of items with specific weights and values, we need to determine the maximum value achievable within a limited capacity, without breaking items (i.e., you either take an item or leave it).
# What is the difference between the Memoization and Tabulation approaches?

# Memoization is a top-down approach that uses recursion with caching to store intermediate results, avoiding redundant calculations. Tabulation is a bottom-up approach that builds solutions iteratively using a 2D array.
# What does dp[i][j] represent in the tabulation solution?

# In the tabulation solution, dp[i][j] represents the maximum profit achievable with the first i items and a knapsack capacity of j.
# Why do we need the dp table in the memoization approach?

# The dp table stores results of subproblems (for different item counts and capacities), which avoids recalculating the values of already-solved subproblems, improving efficiency.
# How does the code determine which items were selected in the final solution?

# The Knapsack_using_DP function traces back through the dp table to see which items contribute to the optimal solution by checking if values differ between current and previous states.
# Explain how max(val[n - 1] + ... , ...) works in the code.

# This part checks if including the current item increases the profit more than excluding it. It adds the value of the current item to the profit of the remaining capacity, then takes the maximum of including or excluding.
# What is the time complexity of this DP-based 0-1 Knapsack solution?

# The time complexity is O(n * W), where n is the number of items and W is the knapsack capacity, as it fills an n x W table.
# What is the difference between 0-1 and fractional knapsack problems?

# In a 0-1 knapsack problem, items cannot be divided, so each item is either fully included or excluded. In a fractional knapsack problem, items can be divided into fractions to maximize value within the capacity.
# How does this program handle the base case?

# In both memoization and tabulation approaches, the base case is defined as having zero capacity or zero items left to consider, resulting in a value of zero for those conditions.
# What does the lambda function in the fractional knapsack code do?

# In the fractional knapsack code, the lambda function sorts items by their value-to-weight ratio in descending order to maximize value per unit weight.
