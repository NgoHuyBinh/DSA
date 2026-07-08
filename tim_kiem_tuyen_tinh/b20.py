def allocate_books(p, m):
    if m > len(p):
        return -1 
        
    def check(max_pages):
        students = 1
        current_pages = 0
        for pages in p:
            if current_pages + pages > max_pages:
                students += 1
                current_pages = pages
            else:
                current_pages += pages
        return students <= m

    left, right = max(p), sum(p)
    ans = right
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            ans = mid
            right = mid - 1 
        else:
            left = mid + 1
    return ans

p = [12, 34, 67, 90]
print(allocate_books([12, 34, 67, 90], 2))