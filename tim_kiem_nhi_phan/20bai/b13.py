def tim_kiem_ten(ds, ten_can_tim):
    for i in range(len(ds)):
        if ds[i].lower() == ten_can_tim.lower():
            return i
    return -1

ds_sinh_vien = ["An", "Bình", "Châu", "Minh Anh"]
ten_1 = "an"
print(f"Tìm '{ten_1}': Vị trí tìm thấy là {tim_kiem_ten(ds_sinh_vien, ten_1)}") 
ten_2 = "bÌnH"
print(f"Tìm '{ten_2}': Vị trí tìm thấy là {tim_kiem_ten(ds_sinh_vien, ten_2)}") 
ten_3 = "Nhật"
print(f"Tìm '{ten_3}': Vị trí tìm thấy là {tim_kiem_ten(ds_sinh_vien, ten_3)}") 
