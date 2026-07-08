def demonstrate_loop_invariant(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
        print(f"Lượt {i+1}: {a}")

demonstrate_loop_invariant([4, 1, 3, 2])