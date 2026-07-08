def sort_students(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j][1] < a[j+1][1] or (a[j][1] == a[j+1][1] and a[j][0] > a[j+1][0]):
                a[j], a[j+1] = a[j+1], a[j]
    return a

a = [('An', 8), ('Ba', 9), ('Cu', 8)]
print(sort_students(a))