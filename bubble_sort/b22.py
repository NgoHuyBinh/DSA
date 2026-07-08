def early_exit_bubble_sort(a):
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break

def bubble_sort_limited_k(a):
    import time
    start = time.time()
    early_exit_bubble_sort(a)
    end = time.time()
    return end - start

a = [i + (1 if i%2==0 else -1) for i in range(10000)] 
time_taken = bubble_sort_limited_k(a)

print(f"Mảng 10^4 chạy mất {time_taken:.5f}s (rất nhanh)")