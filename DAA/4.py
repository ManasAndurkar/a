# Write a program to solve a 0-1 Knapsack problem using dynamic programming

# Path: 4.py

# Write a program to solve a 0-1 Knapsack problem using dynamic programming


def knapsack_dp(w, v, W):  # w = weights, v = values, W = capacity
    n = len(w)
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                K[i][j] = 0
            elif w[i - 1] <= j:
                K[i][j] = max(v[i - 1] + K[i - 1][j - w[i - 1]], K[i - 1][j])
            else:
                K[i][j] = K[i - 1][j]
    return K[n][W]


capacity = int(input("Enter the capacity: "))
n = int(input("Enter the number of items: "))
weights = []
values = []
for i in range(n):
    weight, value = [int(x) for x in input("Enter the weight and value of item {}: ".format(i + 1)).split()]
    weights.append(weight)
    values.append(value)
total_value = knapsack_dp( weights, values ,capacity)
print("Max Profit can get is : ", total_value)