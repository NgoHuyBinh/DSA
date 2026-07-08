def find_min_rotated(a):
    left, right = 0, len(a) - 1
    if a[left] <= a[right]:
        return a[left]
        
    while left <= right:
        mid = (left + right) // 2
        if a[mid] > a[right]:
            left = mid + 1
        else:
            right = mid
            
        if left == right:
            return a[left]

a = [3, 4, 5, 1, 2]
print(find_min_rotated([3, 4, 5, 1, 2]))