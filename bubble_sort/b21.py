def stable_bubble_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j][0] > a[j+1][0]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

def check_stability():
    a = [(2, 'a'), (1, 'b'), (2, 'c')]
    stable_bubble_sort(a)
    return a

print("Kết quả Bài 21:", check_stability())