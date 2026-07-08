def last_occurrence(a, x):
    left, right = 0, len(a) - 1
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            ans = mid
            left = mid + 1  # Tìm tiếp sang bên phải
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return ans
a = [1, 2, 2, 2, 3]
print(last_occurrence([1, 2, 2, 2, 3], 2))