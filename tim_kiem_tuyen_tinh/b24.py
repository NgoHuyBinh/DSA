def min_max_gas_dist(x, k):
    def check(max_dist):
        stations_needed = 0
        for i in range(len(x) - 1):
            stations_needed += int((x[i+1] - x[i]) / max_dist)
        return stations_needed <= k

    left = 0.0
    right = float(x[-1] - x[0])
    
    for _ in range(80):
        mid = (left + right) / 2.0
        if check(mid):
            right = mid
        else:
            left = mid
            
    return round(left, 1)

print(min_max_gas_dist([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9))