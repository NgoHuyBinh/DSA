def tim_kiem_linh_can(a, x):
    a.append(x)
    i = 0
    while a[i] != x:
        i += 1
    if i < len(a):
        return i
    return -1
mang_so = [10, 22, 28, 29, 40]
x = 29

vi_tri = tim_kiem_linh_can(mang_so, x)
print(f"Mảng gốc không bị thay đổi: {mang_so}")
print(f"Vị trí tìm thấy {x} bằng lính canh là: {vi_tri}") 