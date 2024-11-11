class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def fractionalKnapsack(w, arr):
    arr.sort(key=lambda x: x.profit/x.weight, reverse=True)
    finalValue = 0.0
    for item in arr:
        if w >= item.weight:
            finalValue += item.profit
            w -= item.weight
        else:
            finalValue += item.profit * (w/item.weight)
            break
    return finalValue

if __name__ == "__main__":
    n = int(input("Enter number of items-\n"))
    arr = []
    for i in range(n):
        profit = int(input("Enter profit of item " + str(i + 1) + "-\n"))
        weight = int(input("Enter weight of item " + str(i + 1) + "-\n"))
        arr.append(Item(profit, weight))
    w = int(input("Enter capacity of knapsack-\n"))
    print("Maximum value in knapsack: ", fractionalKnapsack(w, arr))
# What is the Fractional Knapsack Problem?
# The Fractional Knapsack Problem involves selecting items with given weights and values to maximize the total value in a knapsack that has a fixed weight capacity, allowing for fractional amounts of items.

# The knapsack is a common problem in combinatorial optimization, which refers to a scenario where a person has a knapsack (or backpack) with a limited capacity, and they need to decide which items to include in the knapsack to maximize the total value.

# Types of Knapsack Problems:

# 0/1 Knapsack: You can either take the whole item or leave it (no fractions). Each item can only be included once.
# Fractional Knapsack: You can take fractions of an item. This means you can split an item and take part of it if it doesn’t fit completely.
# Bounded Knapsack: There are limits on how many of each item you can include.
# Unbounded Knapsack: You can take an unlimited number of each item.

# Applications:
# The knapsack problem has various applications, including resource allocation, budget management, and cargo loading, where you want to optimize the selection of items based on their value relative to their weight.

# Items: Each item has a weight and a value. The goal is to maximize the total value of the items selected.

# Capacity: The knapsack has a maximum weight capacity. The total weight of the selected items must not exceed this capacity.

# What are the time and space complexities of this solution?
# The time complexity is O(n log n) due to sorting the items, and the space complexity is O(n) for storing the items in the list.

# What will be the output of the code if all items can fit into the knapsack?
# The output will be the sum of the values of all items since the knapsack can hold their total weight without exceeding the capacity.

# Can this approach be applied to the 0/1 Knapsack Problem?
# No, this approach cannot be applied to the 0/1 Knapsack Problem, where items cannot be divided; a different method, such as dynamic programming, is used for that case.
