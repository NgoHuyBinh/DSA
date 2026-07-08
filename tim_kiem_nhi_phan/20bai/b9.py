def tim_tat_ca(a, x):
    danh_sach_vi_tri = []
    for i in range(len(a)):
        if a[i] == x:
            danh_sach_vi_tri.append(i)
    return danh_sach_vi_tri

mang_1 = [4, 1, 4, 9, 4]
x1 = 4
print(f"Mảng: {mang_1}, x = {x1}")
print("Kết quả vị trí:", tim_tat_ca(mang_1, x1))  

print("-" * 30)

mang_2 = [1, 2, 3, 7, 8]
x2 = 5
print(f"Mảng: {mang_2}, x = {x2}")
print("Kết quả vị trí:", tim_tat_ca(mang_2, x2)) 