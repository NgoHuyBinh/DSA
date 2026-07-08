def tim_sinh_vien_theo_ma(danh_sach_sv, ma_can_tim):
    for sv in danh_sach_sv:
        if sv["ma_sv"] == ma_can_tim:
            print(f"Mã SV: {sv['ma_sv']}")
            print(f"Họ tên: {sv['ho_ten']}")
            print(f"Điểm trung bình: {sv['diem_tb']}")
            return 
    print(f"Không tìm thấy sinh viên nào có mã '{ma_can_tim}'.")
ds_lop_hoc = [
    {"ma_sv": "SV001", "ho_ten": "Nguyễn Văn An", "diem_tb": 8.0},
    {"ma_sv": "SV002", "ho_ten": "Trần Thị Bình", "diem_tb": 7.0},
    {"ma_sv": "SV003", "ho_ten": "Lê Bảo Châu", "diem_tb": 9.0}
]

tim_sinh_vien_theo_ma(ds_lop_hoc, "SV001")