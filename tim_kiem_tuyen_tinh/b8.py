def my_sqrt(n):
    if n < 2:
        return n
    left, right = 1, n // 2
    ans = 1
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans

n = 8 
print(my_sqrt(8))