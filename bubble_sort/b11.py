def sort_by_absolute(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if abs(a[j]) > abs(a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
    return a

a = [-3, 1, 2, 2]
print(sort_by_absolute(a))