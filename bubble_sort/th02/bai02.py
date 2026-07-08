# Bubble Sort - sắp xếp nổi bọt
def bubble_sort(arr):
    # vòng ngoài: đi qua từng phần tử
    for i in range(len(arr)):
        # vòng trong: so sánh các cặp liền kề
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                # hoán đổi nếu phần trước lớn hơn phần sau
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Mảng cần sắp xếp
arr = [60,32,15,12,52,71,90,-1,-10,-30,-155,75]

# Gọi hàm sắp xếp
bubble_sort(arr)

# In mảng sau khi sắp xếp
print(arr)
