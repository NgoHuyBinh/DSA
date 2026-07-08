def single_non_duplicate(a):
    left, right = 0, len(a) - 1
    while left < right:
        mid = (left + right) // 2
        if mid % 2 == 1:
            mid -= 1
        if a[mid] == a[mid + 1]:
            left = mid + 2
        # Ngược lại, nó nằm ở bên trái
        else:
            right = mid
    return a[left]

a = [1, 1, 2, 3, 3, 4, 4]
print(single_non_duplicate([1, 1, 2, 3, 3, 4, 4]))