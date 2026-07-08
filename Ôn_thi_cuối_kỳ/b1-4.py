import math

# ==========================================
# CÂU 1: CHIA MẢNG - TÌM KIẾM NHỊ PHÂN
# ==========================================
def check_xe_tai(khoi_luong, tai_trong_max, k_xe):
    so_xe_can = 1
    tong_hien_tai = 0
    for kien_hang in khoi_luong:
        if tong_hien_tai + kien_hang > tai_trong_max:
            so_xe_can += 1
            tong_hien_tai = kien_hang
            if so_xe_can > k_xe:
                return False
        else:
            tong_hien_tai += kien_hang
    return True

def tim_tai_trong_toi_thieu(W, K):
    left = max(W)   # Xe phải chở được kiện nặng nhất
    right = sum(W)  # Tệ nhất là 1 xe cân hết
    ans = right
    
    while left <= right:
        mid = (left + right) // 2
        if check_xe_tai(W, mid, K):
            ans = mid
            right = mid - 1  # Thử tìm tải trọng nhỏ hơn
        else:
            left = mid + 1   # Thiếu xe, phải tăng tải trọng
    return ans

W = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
K = 5
tai_trong = tim_tai_trong_toi_thieu(W, K)
print(f"Cau 1: Tai trong toi thieu cua mot xe la: {tai_trong}")


# ==========================================
# CÂU 2: THUẬT TOÁN SẮP XẾP (INSERTION SORT)
# ==========================================
def insertion_sort_dem_shift(mang):
    a = mang.copy()
    n = len(a)
    tong_shift = 0
    for i in range(1, n):
        khoa = a[i]
        j = i - 1
        while j >= 0 and a[j] > khoa:
            a[j + 1] = a[j]
            j -= 1
            tong_shift += 1
        a[j + 1] = khoa
    return tong_shift

A = [5, 2, 4, 6, 1, 3]
so_shift = insertion_sort_dem_shift(A)
print(f"Cau 2: Tong so lan shift phan tu la: {so_shift} (Bang dung so cap nghich the)")


# ==========================================
# CÂU 3: ĐỒ THỊ & THUẬT TOÁN DIJKSTRA (PHẢN VÍ DỤ)
# ==========================================
def dijkstra_phan_vi_du():
    # A = 0, B = 1, C = 2
    do_thi = {
        0: [(1, 4), (2, 1)],  # A -> B (4), A -> C (1)
        2: [(1, -2)],         # C -> B (-2)
        1: []                 # B khong co canh ra
    }
    
    khoang_cach = {0: 0, 1: float('inf'), 2: float('inf')}
    chot_dinh = set()
    
    chua_duyet = [0, 1, 2]
    while chua_duyet:
        u = min(chua_duyet, key=lambda x: khoang_cach[x])
        chua_duyet.remove(u)
        chot_dinh.add(u)
        
        for ke, trong_so in do_thi[u]:
            if ke not in chot_dinh:
                kc_moi = khoang_cach[u] + trong_so
                if kc_moi < khoang_cach[ke]:
                    khoang_cach[ke] = kc_moi
                    
    return khoang_cach

kq_dijkstra = dijkstra_phan_vi_du()
print(f"Cau 3: Ket qua Dijkstra (bi sai cho dinh B): {kq_dijkstra} (Dung ra A->B phai la 1)")


# ==========================================
# CÂU 4: ỨNG DỤNG NGĂN XẾP (MONOTONIC STACK)
# ==========================================
def daily_temperatures(T):
    n = len(T)
    ket_qua = [0] * n
    stack = []  # Luu tru chi so (index) cua cac ngay
    
    for i in range(n):
        while stack and T[i] > T[stack[-1]]:
            idx_cu = stack.pop()
            ket_qua[idx_cu] = i - idx_cu  # Tinh so ngay phai cho
        stack.append(i)
        
    return ket_qua

T = [73, 74, 75, 71, 69, 72, 76, 73]
kq_ngay_cho = daily_temperatures(T)
print(f"Cau 4: Mang ket qua so ngay cho la: {kq_ngay_cho}")