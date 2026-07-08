def count_comparisons(a):
    comps = 0
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            comps += 1
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return comps

a = [1, 2, 3]
print(count_comparisons(a))