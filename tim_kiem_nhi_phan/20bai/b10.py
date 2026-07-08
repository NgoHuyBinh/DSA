def vi_tri_cuoi_cung(a, x):
    for i in range(len(a) - 1, -1, -1):
        if a[i] == x:
            return i
    return -1

mang_test = [4, 1, 4, 9, 4, 2]
x = 4

ket_qua = vi_tri_cuoi_cung(mang_test, x)
print(f"Mảng: {mang_test}, Số cần tìm: {x}")
print("Vị trí xuất hiện cuối cùng là:", ket_qua) # chạy kết quả có x trong mảng
print("Kết quả khi không tìm thấy:", vi_tri_cuoi_cung(mang_test, 5)) # chạy kết quả ko có x trong mảng