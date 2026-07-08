def kth_smallest(matrix, k):
    n = len(matrix)
    
    def count_less_equal(mid):
        count = 0
        col = n - 1
        for row in range(n):
            while col >= 0 and matrix[row][col] > mid:
                col -= 1
            count += (col + 1)
        return count

    left, right = matrix[0][0], matrix[n-1][n-1]
    ans = left
    
    while left <= right:
        mid = (left + right) // 2
        if count_less_equal(mid) >= k:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans

matrix = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]
print(kth_smallest(matrix, 8))