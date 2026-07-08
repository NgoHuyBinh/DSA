def split_array(a, k):
    def check(max_sum):
        chunks = 1
        current_sum = 0
        for num in a:
            if current_sum + num > max_sum:
                chunks += 1
                current_sum = num
            else:
                current_sum += num
        return chunks <= k

    left, right = max(a), sum(a)
    ans = right
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans

a = [7, 2, 5, 10, 8]
print(split_array([7, 2, 5, 10, 8], 2))