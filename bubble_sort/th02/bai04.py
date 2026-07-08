# Bubble Sort - sắp xếp nổi bọt giảm dần
def bubble_sort(arr):
    # vòng ngoài: đi qua từng phần tử
    for i in range(len(arr)):
        # vòng trong: so sánh các cặp liền kề
        for j in range(len(arr) - 1):
            if arr[j] < arr[j + 1]:  # đổi dấu > thành <
                # hoán đổi nếu phần trước nhỏ hơn phần sau
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Mảng cần sắp xếp
arr = [120, 35, 60, 42, 280, 7, 15, 19]

# Gọi hàm sắp xếp
bubble_sort(arr)

# In mảng sau khi sắp xếp
print("Mảng sắp xếp từ lớn đến bé:", arr)