def count_inversions_fast(arr):
    if len(arr) <= 1: return arr, 0
    mid = len(arr) // 2
    left, inv_left = count_inversions_fast(arr[:mid])
    right, inv_right = count_inversions_fast(arr[mid:])
    merged, inv_merge = [], 0
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv_merge += len(left) - i
            j += 1
    merged += left[i:] + right[j:]
    return merged, inv_left + inv_right + inv_merge

a = [5, 4, 3, 2, 1]
_, swaps = count_inversions_fast(a)
print(swaps)