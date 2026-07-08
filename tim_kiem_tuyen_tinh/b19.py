def aggressive_cows(x, c):
    x.sort() 
    def check(distance):
        count = 1
        last_position = x[0]
        for i in range(1, len(x)):
            if x[i] - last_position >= distance:
                count += 1
                last_position = x[i]
                if count >= c:
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

x = [1, 2, 4, 8, 9], c = 3 
print(aggressive_cows([1, 2, 4, 8, 9], 3))