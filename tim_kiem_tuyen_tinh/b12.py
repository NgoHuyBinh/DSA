def find_peak_element(a):
    left, right = 0, len(a) - 1
    while left < right:
        mid = (left + right) // 2
        if a[mid] < a[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left

a = [1, 2, 3, 1]
print(find_peak_element([1, 2, 3, 1]))