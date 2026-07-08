def tim_min_max_mot_lan_duyet(a):
    if len(a) == 0:
        return None, -1, None, -1
    gia_tri_max = a[0]
    vi_tri_max = 0
    
    gia_tri_min = a[0]
    vi_tri_min = 0
    for i in range(1, len(a)):
        if a[i] > gia_tri_max:
            gia_tri_max = a[i]
            vi_tri_max = i
        if a[i] < gia_tri_min:
            gia_tri_min = a[i]
            vi_tri_min = i
    return gia_tri_min, vi_tri_min, gia_tri_max, vi_tri_max
mang_so = [34, 12, 89, 5, 76, 95, 21]

g_min, v_min, g_max, v_max = tim_min_max_mot_lan_duyet(mang_so)

print(f"Mảng xét: {mang_so}\n")
print(f"Giá trị NHỎ nhất: {g_min} (ở vị trí chỉ số: {v_min})")
print(f"Giá trị LỚN nhất: {g_max} (ở vị trí chỉ số: {v_max})")