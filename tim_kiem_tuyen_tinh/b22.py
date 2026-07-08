def find_median_sorted_arrays(a, b):
   
    if len(a) > len(b):
        a, b = b, a
        
    m, n = len(a), len(b)
    left, right = 0, m
    
    while left <= right:
        partition_a = (left + right) // 2
        partition_b = (m + n + 1) // 2 - partition_a
        max_left_a = float('-inf') if partition_a == 0 else a[partition_a - 1]
        min_right_a = float('inf') if partition_a == m else a[partition_a]
        
        max_left_b = float('-inf') if partition_b == 0 else b[partition_b - 1]
        min_right_b = float('inf') if partition_b == n else b[partition_b]
        if max_left_a <= min_right_b and max_left_b <= min_right_a:
            if (m + n) % 2 == 1:
                return float(max(max_left_a, max_left_b))
            else:
                return (max(max_left_a, max_left_b) + min_right_a if min_right_a < min_right_b else max(max_left_a, max_left_b) + min_right_b) / 2.0
                
        elif max_left_a > min_right_b:
            right = partition_a - 1
        else:
            left = partition_a + 1

a = [1, 3]
b = [2] 
print(find_median_sorted_arrays([1, 3], [2]))