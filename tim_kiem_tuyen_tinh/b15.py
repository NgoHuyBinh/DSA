def find_closest_elements(a, k, x):
    # Tìm vị trí bắt đầu
    left, right = 0, len(a) - k
    while left < right:
        mid = (left + right) // 2
        if x - a[mid] > a[mid + k] - x:
            left = mid + 1
        else:
            right = mid
    return a[left : left + k]

a = [1, 2, 3, 4, 5], k = 4, x = 3
print(find_closest_elements([1, 2, 3, 4, 5], 4, 3))