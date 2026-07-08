# BÀI 16
# Online Insertion Sort
def bai_16(stream):
    result = []

    for x in stream:
        result.append(x)

        i = len(result) - 1

        while i > 0 and result[i - 1] > result[i]:
            result[i - 1], result[i] = result[i], result[i - 1]
            i -= 1

        print(result)

bai_16([5,2,8,1])

print("-" * 30)

# BÀI 17
# Mảng gần sắp xếp
def bai_17(a):
    shifts = 0

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            shifts += 1
            j -= 1

        a[j + 1] = key

    return shifts

print("Bài 17:", bai_17([1,2,4,3,5]))

print("-" * 30)

# BÀI 18
# Chèn từ cuối hay đầu
def bai_18():
    print("Dò từ phải sang trái hiệu quả hơn với dữ liệu gần sắp xếp.")
    print("Vì phần tử thường chỉ phải dịch chuyển một đoạn ngắn.")

bai_18()

print("-" * 30)

# BÀI 19
# Gnome Sort
def bai_19(a):
    i = 0

    while i < len(a):
        if i == 0 or a[i] >= a[i - 1]:
            i += 1
        else:
            a[i], a[i - 1] = a[i - 1], a[i]
            i -= 1

    return a

print("Bài 19:", bai_19([3,2,1]))

print("-" * 30)

# BÀI 20
# Shell Sort
def bai_20(a):
    n = len(a)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = a[i]
            j = i

            while j >= gap and a[j - gap] > temp:
                a[j] = a[j - gap]
                j -= gap

            a[j] = temp

        gap //= 2

    return a

print("Bài 20:", bai_20([8,5,3,7,6,2,1,4]))

print("-" * 30)
