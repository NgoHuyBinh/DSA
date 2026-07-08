def bai_16(a):
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if abs(a[j]) < abs(a[min_idx]): min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a
print(bai_16([-3, 1, -2, 2]))

print("-"*30)

def bai_15(a, k):
    n = len(a)
    for i in range(min(k, n)):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]: min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a
print(bai_15([5, 3, 1, 4, 2], 2))
def bai_17(a, k):
    bai_15(a, k)
    return a[k - 1]
print("Bài 17: Phần tử nhỏ thứ 3 =", bai_17([7, 2, 5, 1, 9], 3))

print("-"*30)

def bai_18():
    print("Bài 18: Selection (O(n)) ít swap hơn Bubble (O(n^2))")
bai_18()

print("-"*30)

def bai_19():
    print("Bài 19: maxIdx trùng i đã được xử lý ở if max_idx == i trong Bài 9")
bai_19()

print("-"*30)

def bai_20():
    print("Bài 20: Heap Sort tối ưu hơn với O(n log n)")
bai_20()