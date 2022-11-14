#  Write a program to solve a fractional Knapsack problem using a greedy method.


def knapsack(capacity, weights, values):
    value_per_unit_weight = [v / w for v, w in zip(values, weights)]
    sorted_indices = sorted(range(len(value_per_unit_weight)), key=lambda k: value_per_unit_weight[k], reverse=True)
    total_value = 0
    for i in sorted_indices:
        if weights[i] <= capacity:
            capacity -= weights[i]
            total_value += values[i]
        else:
            fraction = capacity / weights[i]
            total_value += values[i] * fraction
            break
    return total_value



capacity = int(input("Enter the capacity: "))
n = int(input("Enter the number of items: "))
weights = []
values = []
for i in range(n):
    weight, value = [int(x) for x in input("Enter the weight and value of item {}: ".format(i + 1)).split()]
    weights.append(weight)
    values.append(value)
total_value = knapsack(capacity, weights, values)



total_value = knapsack(50 , [30,20,10] , [60,50,40] )


print("The total value is", total_value)


