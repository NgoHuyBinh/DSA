def first_occurrence(a, x):
    left, right = 0, len(a) - 1
    res = -1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            res = mid
            right = mid - 1  # Tiếp tục tìm về phía bên trái
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return res

def last_occurrence(a, x):
    left, right = 0, len(a) - 1
    res = -1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            res = mid
            left = mid + 1  # Tiếp tục tìm về phía bên phải
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return res

def count_occurrences(a, x):
    first = first_occurrence(a, x)
    if first == -1:
        return 0
    last = last_occurrence(a, x)
    return last - first + 1

a = [1, 2, 2, 2, 3]
print(count_occurrences(a, 2)) 