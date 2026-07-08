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

def benchmark():
    import time
    n = 1000
    sorted_arr = list(range(n))
    reverse_arr = sorted_arr[::-1]
    
    t0 = time.time(); early_exit_bubble_sort(sorted_arr.copy()); t1 = time.time()
    t2 = time.time(); early_exit_bubble_sort(reverse_arr.copy()); t3 = time.time()
    
    print(f" Best = {t1-t0:.5f}s, Worst = {t3-t2:.5f}s")
benchmark()