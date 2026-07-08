# BÀI 1
# Chèn một phần tử vào mảng đã sắp xếp
def bai_1(a, x):
    a.append(x)
    i = len(a) - 2

    while i >= 0 and a[i] > x:
        a[i + 1] = a[i]
        i -= 1

    a[i + 1] = x
    return a

print("Bài 1:", bai_1([1, 3, 5, 7], 4))

print("-" * 30)


# BÀI 2
# Insertion Sort tăng dần
def bai_2(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

    return a

print("Bài 2:", bai_2([5, 2, 4, 6, 1, 3]))

print("-" * 30)

# BÀI 3
# Sắp xếp giảm dần
def bai_3(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] < key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

    return a

print("Bài 3:", bai_3([5, 2, 4, 6, 1]))

print("-" * 30)


# BÀI 4
# In mảng sau mỗi bước chèn
def bai_4(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key
        print(a)

print("Bài 4:")
bai_4([3, 1, 2])

print("-" * 30)


# BÀI 5
# Đếm số lần dịch chuyển
def bai_5(a):
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

print("Bài 5:", bai_5([3, 2, 1]))

print("-" * 30)