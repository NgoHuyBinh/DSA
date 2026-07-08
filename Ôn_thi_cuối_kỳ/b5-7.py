from collections import deque

# ==========================================
# CÂU 5: GIÁ TRỊ NHỎ NHẤT TRONG CỬA SỔ TRƯỢT
# ==========================================
def min_cua_so_truot(mang, k):
    if not mang or k <= 0:
        return []
    
    ket_qua = []
    dq = deque()  # Lưu trữ chỉ số (index), giữ giá trị tăng dần đơn điệu
    
    for i in range(len(mang)):
        # 1. Loại bỏ các chỉ số đã nằm ngoài cửa sổ trượt hiện tại
        if dq and dq[0] < i - k + 1:
            dq.popleft()
            
        # 2. Loại bỏ các phần tử LỚN HƠN hoặc BẰNG phần tử hiện tại sắp chèn vào
        while dq and mang[dq[-1]] >= mang[i]:
            dq.pop()
            
        dq.append(i)
        
        # In trạng thái Deque ở 3 bước dịch chuyển đầu tiên theo yêu cầu
        if i < 3:
            print(f"i = {i} (gia tri = {mang[i]}): Deque hien tai luu index = {list(dq)} "
                  f"(tuong ung gia tri = {[mang[x] for x in dq]})")
        
        # 3. Thêm vào kết quả khi cửa sổ đã quét đủ kích thước k
        if i >= k - 1:
            ket_qua.append(mang[dq[0]])
            
    return ket_qua

A = [4, 2, 12, 11, -5, 8, 1, 5, 6]
k = 3
print("--- Mo phong 3 buoc dau Cau 5 ---")
kq_min = min_cua_so_truot(A, k)
print(f"-> Mang ket qua cuoi cung: {kq_min}\n")


# ==========================================
# CÂU 6: LÝ THUYẾT FLOYD (MÔ PHỎNG PHÁT HIỆN CHU TRÌNH)
# ==========================================
class Node:
    def __init__(self, du_lieu):
        self.du_lieu = du_lieu
        self.tiep_theo = None

def tim_nut_bat_dau_chu_trinh(head):
    if not head or not head.tiep_theo:
        return None
        
    rua = head
    tho = head
    co_chu_trinh = False
    
    # Giai đoạn 1: Phát hiện chu trình
    while tho and tho.tiep_theo:
        rua = rua.tiep_theo
        tho = tho.tiep_theo.tiep_theo
        if rua == tho:
            co_chu_trinh = True
            break
            
    if not co_chu_trinh:
        return None
        
    # Giai đoạn 2: Đưa 1 con trỏ về Head, cả 2 đi đồng tốc 1 bước
    rua = head
    while rua != tho:
        rua = rua.tiep_theo
        tho = tho.tiep_theo
        
    return rua  # Nút bắt đầu chu trình
n1, n2, n3, n4, n5 = Node(1), Node(2), Node(3), Node(4), Node(5)
n1.tiep_theo = n2
n2.tiep_theo = n3
n3.tiep_theo = n4
n4.tiep_theo = n5
n5.tiep_theo = n3  # Tạo chu trình tại nút số 3

nut_goc = tim_nut_bat_dau_chu_trinh(n1)
print(f"Cau 6: Nut bat dau chu trinh tim duoc bang thuat toan la: {nut_goc.du_lieu if nut_goc else None}\n")


# ==========================================
# CÂU 7: BẢNG BĂM & MẢNG CỘNG DỒN (TỔNG BẰNG S)
# ==========================================
def dem_mang_con_tong_s(mang, S):
    bang_bam = {0: 1}
    tong_tien_to = 0
    so_luong_mang_con = 0
    
    for phan_tu in mang:
        tong_tien_to += phan_tu
        phan_bu = tong_tien_to - S
        
        if phan_bu in bang_bam:
            so_luong_mang_con += bang_bam[phan_bu]
            
        if tong_tien_to in bang_bam:
            bang_bam[tong_tien_to] += 1
        else:
            bang_bam[tong_tien_to] = 1
            
    return so_luong_mang_con

A_c7 = [3, 4, 7, 2, -3, 1, 4, 2]
S = 7
kq_c7 = dem_mang_con_tong_s(A_c7, S)
print(f"Cau 7: So luong mang con co tong bang {S} la: {kq_c7}")