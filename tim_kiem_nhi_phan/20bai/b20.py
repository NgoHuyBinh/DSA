danh_ba = [
    {"ten": "Nguyen Van An", "sdt": "0901234567"},
    {"ten": "Tran Thi Binh", "sdt": "0918888888"},
    {"ten": "Le Hoang Chau", "sdt": "0907776665"}
]

# Chức năng 1: Thêm liên hệ
def them_lien_he(ten, sdt):
    lien_he_moi = {"ten": ten, "sdt": sdt}
    danh_ba.append(lien_he_moi)
    print(f"Da them thanh cong: {ten} - {sdt}")

# Chức năng 2: Tìm số điện thoại theo tên (không phân biệt hoa thường)
def tim_sdt_theo_ten(ten_can_tim):
    for lh in danh_ba:
        if lh["ten"].lower() == ten_can_tim.lower():
            print(f"Tim thay so dien thoai cua '{lh['ten']}': {lh['sdt']}")
            return
    print(f"Khong tim thay lien he nao co ten '{ten_can_tim}'.")

# Chức năng 3: Tìm tên theo số điện thoại
def tim_ten_theo_sdt(sdt_can_tim):
    for lh in danh_ba:
        if lh["sdt"] == sdt_can_tim:
            print(f"So dien thoai {sdt_can_tim} la cua: {lh['ten']}")
            return
    print(f"Khong tim thay ten ung voi so dien thoai '{sdt_can_tim}'.")

# Chức năng 4: Đếm số liên hệ theo đầu số
def dem_theo_dau_so(dau_so):
    dem = 0
    for lh in danh_ba:
        if lh["sdt"].startswith(dau_so):
            dem += 1
    print(f"Co {dem} lien he co so dien thoai bat dau bang dau so '{dau_so}'.")


while True:
    print("\n" + "="*15 + " QUẢN LÝ DANH BẠ " + "="*15)
    print("1. Thêm liên hệ mới")
    print("2. Tìm số điện thoại theo tên")
    print("3. Tìm tên theo số điện thoại")
    print("4. Đếm số liên hệ theo đầu số")
    print("5. Thoát chương trình")
    print("="*47)
    
    luachon = input("Nhập lựa chọn của bạn (1-5): ")
    
    if luachon == "1":
        ten = input("Nhập họ tên: ")
        sdt = input("Nhập số điện thoại: ")
        them_lien_he(ten, sdt)
        
    elif luachon == "2":
        ten_tim = input("Nhập tên cần tìm số: ")
        tim_sdt_theo_ten(ten_tim)
        
    elif luachon == "3":
        sdt_tim = input("Nhập số điện thoại cần tìm tên: ")
        tim_ten_theo_sdt(sdt_tim)
        
    elif luachon == "4":
        dau_so = input("Nhập đầu số cần đếm (ví dụ 090): ")
        dem_theo_dau_so(dau_so)
        
    elif luachon == "5":
        print("Tam biet! Chuong trinh da ket thuc.")
        break
        
    else:
        print("Lua chon khong hop le! Vui long nhap lai tu 1 den 5.")