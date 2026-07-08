def max_distance_magnetic_force(x, m):
    x.sort()
    
    def check(force):
        count = 1
        last_pos = x[0]
        for i in range(1, len(x)):
            if x[i] - last_pos >= force:
                count += 1
                last_pos = x[i]
                if count >= m:
                    return True
        return False

    left = 1
    right = x[-1] - x[0]
    ans = 0
    
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans

print(max_distance_magnetic_force([1, 2, 3, 4, 7], 3))