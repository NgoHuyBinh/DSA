def is_sorted_after_k_passes(a, k):
    n = len(a)
    for i in range(min(k, n)):
        for j in range(0, n - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return all(a[m] <= a[m+1] for m in range(len(a)-1))

a = [3, 2, 1]
k = 1
print(str(is_sorted_after_k_passes(a, k)).lower())