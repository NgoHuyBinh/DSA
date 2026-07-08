def ship_within_days(w, d):
    def check(capacity):
        days = 1
        current_weight = 0
        for weight in w:
            if current_weight + weight > capacity:
                days += 1
                current_weight = weight
            else:
                current_weight += weight
        return days <= d

    left, right = max(w), sum(w)
    ans = right
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            ans = mid
            right = mid - 1  # Thử tìm sức chứa nhỏ hơn
        else:
            left = mid + 1
    return ans

w = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], D = 5
print(ship_within_days([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))