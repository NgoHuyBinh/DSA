def early_exit_bubble_sort(a):
    a = a[:]
    passes = 0

    for i in range(len(a)-1):
        swapped = False

        for j in range(len(a)-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True

        passes += 1

        if not swapped:
            break

    return passes

def count_passes_needed(a):
    return early_exit_bubble_sort(a)

a = [2, 1, 3, 4]
print(count_passes_needed(a))