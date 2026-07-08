def bai_1(a):
    min_idx = a.index(min(a))
    a[0], a[min_idx] = a[min_idx], a[0]
    return a
print(bai_1([4, 2, 7, 1, 3]))

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

print("-"*30)

def bai_3(a):
    n = len(a)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if a[j] > a[max_idx]: max_idx = j
        a[i], a[max_idx] = a[max_idx], a[i]
    return a
print(bai_3([5, 2, 4, 6, 1]))

print("-"*30)

def bai_4(a):
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]: min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        print(a)
    return a
print(bai_4([3, 1, 2]))

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