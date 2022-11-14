# Quick Sort


#  using deterministic method

import random


comp = 0

def quick_sort(l):  
    global comp
    if not l:
        return []
    else:
        comp = comp +  1
        pivot = l[len(l) // 2]
        less = [i for i in l if i < pivot]
        greater = [i for i in l if i > pivot]
        pivot  = [i for i in l if i == pivot]
        return quick_sort(less) + pivot + quick_sort(greater)


print(quick_sort([5,2,1,3]))

print("Total comparisons: ", comp)



comp = 0

def qsort(arr):
    global comp
    if not arr: 
        return []
    comp = comp +  1
    pivot = arr[random.choice(range(0, len(arr)))]
    less = qsort([x for x in arr if x < pivot])
    greater = qsort([x for x in arr if x > pivot])
    pivot  = [i for i in arr if i == pivot]
    return less + pivot + greater

print(qsort([5,2,1,3]))
print("Total comparisons: ", comp)