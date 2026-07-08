def bai_6(a):
    n = len(a)
    comps = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comps += 1
            if a[j] < a[min_idx]: min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return comps
print(bai_6([0, 0, 0, 0, 0])) 

print("-"*30)

def bai_2(a):
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]: min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a
print(bai_2([5, 2, 4, 6, 1, 3]))
def bai_7(a):
    return bai_2(a)
print(bai_7(['d', 'a', 'c', 'b']))

print("-"*30)

def bai_8(a, i):
    min_idx = i
    for j in range(i + 1, len(a)):
        if a[j] < a[min_idx]: min_idx = j
    return min_idx
print(bai_8([9, 3, 7, 1, 5], 1))

print("-"*30)

def bai_9(a):
    n = len(a)
    for i in range(n // 2):
        min_idx, max_idx = i, i
        for j in range(i, n - i):
            if a[j] < a[min_idx]: min_idx = j
            if a[j] > a[max_idx]: max_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        if max_idx == i: max_idx = min_idx
        a[n - 1 - i], a[max_idx] = a[max_idx], a[n - 1 - i]
    return a
print(bai_9([5, 1, 4, 2, 8]))

print("-"*30)

def bai_5(a):
    n = len(a)
    swaps = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]: min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swaps += 1
    return swaps
print( bai_5([3, 2, 1]))
def bai_10(a):
    return bai_5(a)
print(bai_10([1, 2, 3]))