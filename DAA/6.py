# Quick Sort


#  using deterministic method

import random


comp = 0

def quick_sort(arr):
    global comp
    if len(arr) <= 1:
        return arr
    else:
        comp = comp +1 
        pivot = arr[len(arr)//2]   # using middle element as pivot
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([10, 5, 2, 3 , 8,78,165,2,65415,615,65,54,4]))

print("Total comparisons: ", comp)


comp = 0
# using random method

def quick_sort(arr):
    global comp
    if len(arr) <= 1:
        return arr
    else:
        comp = comp +1 
        pivot = random.choice(arr)
        less = [i for i in arr if i < pivot]
        greater = [i for i in arr if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

        
print(quick_sort([10, 5, 2, 3 , 8,78,165,2,65415,615,65,54,4]))

print("Total comparisons: ", comp)
