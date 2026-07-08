def one_pass_bubble_sort(a):
    for i in range(len(a) - 1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
    return a

a = [5, 1, 4, 2, 8]
print( one_pass_bubble_sort(a))