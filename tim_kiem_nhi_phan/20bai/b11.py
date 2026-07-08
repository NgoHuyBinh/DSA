def tim_max_va_vi_tri(a):
    # Nếu mảng rỗng thì không có giá trị max
    if len(a) == 0:
        return None, -1
    gia_tri_max = a[0]
    vi_tri_max = 0
    for i in range(1, len(a)):
        if a[i] > gia_tri_max:
            gia_tri_max = a[i]
            vi_tri_max = i
    return gia_tri_max, vi_tri_max

mang_so = [12, 45, 7, 91, 23, 91, 50]

val_max, pos_max = tim_max_va_vi_tri(mang_so)

print(f"Mảng xét: {mang_so}")
print(f"Giá trị lớn nhất là: {val_max}")
print(f"Vị trí (chỉ số) xuất hiện đầu tiên của nó là: {pos_max}")
