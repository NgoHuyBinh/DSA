# Bubble Sort - sắp xếp nổi bọt
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

# Mảng ban đầu
arr = [25, 17, 7, 14, 6, 3, 100, -2, -10, -50]

print("Mảng chưa được sắp xếp là:", arr)

# Gọi hàm sắp xếp
bubble_sort(arr)

print("Mảng được sắp xếp là:", arr)