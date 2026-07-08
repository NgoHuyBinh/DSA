# BÀI 6
# Đếm số lần so sánh
def bai_6(a):
    comps = 0

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0:
            comps += 1

            if a[j] > key:
                a[j + 1] = a[j]
                j -= 1
            else:
                break

        a[j + 1] = key

    return comps

print("Bài 6:", bai_6([1, 2, 3]))

print("-" * 30)

# BÀI 7
# Sắp xếp ký tự
def bai_7(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

    return a

print("Bài 7:", bai_7(['d', 'a', 'c', 'b']))

print("-" * 30)

# BÀI 8
# Trạng thái sau k bước
def bai_8(a, k):
    for i in range(1, min(k + 2, len(a))):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

    return a

print("Bài 8:", bai_8([4, 3, 2, 1], 1))

print("-" * 30)

# BÀI 9
# Binary Insertion Sort
def binary_search(a, key, left, right):
    while left <= right:
        mid = (left + right) // 2

        if a[mid] > key:
            right = mid - 1
        else:
            left = mid + 1

    return left


def bai_9(a):
    for i in range(1, len(a)):
        key = a[i]

        pos = binary_search(a, key, 0, i - 1)

        j = i
        while j > pos:
            a[j] = a[j - 1]
            j -= 1

        a[pos] = key

    return a

print("Bài 9:", bai_9([5, 2, 4, 6, 1, 3]))

print("-" * 30)

# BÀI 10
# Số shift = số nghịch thế
def bai_10(a):
    inversions = 0

    n = len(a)

    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                inversions += 1

    return inversions

print("Bài 10:", bai_10([2, 4, 1, 3]))
print("-" * 30)