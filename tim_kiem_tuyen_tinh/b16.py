def min_eating_speed(piles, h):
    def check(speed):
        hours = 0
        for p in piles:
            hours += (p + speed - 1) // speed 
        return hours <= h

    left, right = 1, max(piles)
    ans = right
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            ans = mid
            right = mid - 1 
        else:
            left = mid + 1
    return ans

piles = [3, 6, 7, 11], h = 8 
print(min_eating_speed([3, 6, 7, 11], 8))