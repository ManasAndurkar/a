# Capacityrite a program to solve a 0-1 Knapsack problem using dynamic programming


def knapsack_dp(w, v, Capacity):  # w = weights, v = values, Capacity = capacity
    n = len(w)
    K = [[0 for x in range(Capacity + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for j in range(Capacity + 1):
            if i == 0 or j == 0:
                K[i][j] = 0
            elif w[i - 1] <= j:   # means remaining capacity is greater than weight of item
                K[i][j] = max(v[i - 1] + K[i - 1][j - w[i - 1]], 
                K[i - 1][j])
    #  getting max from 2 options
    #  1. value of item + value of item that can be accommodated in remaining capacity
            # K[i - 1][j - w[i - 1]]  = k[previous row][remaining capacity]  and 
            #   remaining capacity = current_capacity_filled - weight of item
    #  2. profit at previous row and same column
            else:
                K[i][j] = K[i - 1][j]
    return K[n][Capacity]


# capacity = int(input("Enter the capacity: "))
# n = int(input("Enter the number of items: "))
# weights = []
# values = []
# for i in range(n):
#     weight, value = [int(x) for x in input("Enter the weight and value of item {}: ".format(i + 1)).split()]
#     weights.append(weight)
#     values.append(value)
# total_value = knapsack_dp( weights, values ,capacity)

total_value = knapsack_dp([3,2,1] , [60,50,40] ,5)
print("Max Profit can get is : ", total_value)

print([[0]*2]*3)