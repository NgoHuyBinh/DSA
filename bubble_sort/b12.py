def sort_by_length(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if len(a[j]) > len(a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
    return a

a = ['abc', 'a', 'ab']
print(sort_by_length(a))