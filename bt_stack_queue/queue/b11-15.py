from collections import deque

# --- BÀI 11
def max_cua_so_truot(mang, k):
    if not mang or k <= 0:
        return []
    
    ket_qua = []
    dq = deque()  # Lưu trữ chỉ số (index), giữ giá trị giảm dần đơn điệu
    
    for i in range(len(mang)):
        # Loại bỏ các chỉ số đã nằm ngoài cửa sổ trượt hiện tại
        if dq and dq[0] < i - k + 1:
            dq.popleft()
            
        # Loại bỏ các phần tử nhỏ hơn phần tử hiện tại sắp chèn vào
        while dq and mang[dq[-1]] < mang[i]:
            dq.pop()
            
        dq.append(i)
        
        # Thêm vào kết quả khi cửa sổ đã quét đủ kích thước k
        if i >= k - 1:
            ket_qua.append(mang[dq[0]])
            
    return ket_qua

mang_11 = [1, 3, -1, -3, 5, 3]
print("Bai 11: ", max_cua_so_truot(mang_11, 3))


# --- BÀI 12
def josephus_song_sot(n, k):
    # Đưa n người vào hàng đợi (đánh số từ 1 đến n)
    hang_doi = deque(range(1, n + 1))
    
    while len(hang_doi) > 1:
        # Chuyển k-1 người đầu tiên xuống cuối hàng đợi
        for _ in range(k - 1):
            hang_doi.append(hang_doi.popleft())
        # Loại bỏ người thứ k khỏi vòng tròn
        hang_doi.popleft()
        
    return hang_doi[0]  # Người sống sót cuối cùng

print("Bai 12: ", josephus_song_sot(5, 2))


# --- BÀI 13: HÀNG ĐỢI AMORTIZED O(1) TỪ HAI NGÂN XẾP (CHỨNG MINH LÝ THUYẾT) ---
def phan_tich_ke_toan_amortized():
    # Phân tích bằng phương pháp kế toán (Accounting method):
    # Quy ước chi phí thực tế (Actual cost) của thao tác append/pop trên một Stack đơn lẻ là 1 token.
    # Ta định giá chi phí khấu hao (Amortized charge) cho các thao tác của Queue như sau:
    # 1. Thao tác Enqueue: Trả 2 tokens.
    #    - 1 token dùng để thực hiện việc push trực tiếp vào `in-stack`.
    #    - 1 token còn lại được lưu trữ lại như một khoản "tín dụng" (credit) đính kèm với phần tử đó.
    # 2. Thao tác Dequeue: Trả 0 token từ tài khoản hiện tại (Sử dụng tín dụng tích lũy).
    #    - Trường hợp 1: Nếu `out-stack` đã có sẵn phần tử, chi phí thực tế chỉ là 1 token để pop từ `out-stack`. 
    #                    Khoản này được bù đắp từ phần dư của hệ thống.
    #    - Trường hợp 2: Nếu `out-stack` rỗng, ta phải vét toàn bộ `in-stack` đổ sang. Với mỗi phần tử được chuyển dịch:
    #                    Nó tốn 1 lần pop từ `in-stack` và 1 lần push vào `out-stack` (tổng cộng chi phí thực tế = 2). 
    #                    Chi phí này được chi trả hoàn toàn bằng 1 token tín dụng đã tích lũy từ lúc Enqueue và khoản ký quỹ.
    # Kết luận: Do mỗi phần tử chỉ dịch chuyển qua các stack tối đa 1 lần, tổng chi phí trung bình (Amortized cost) 
    # cho bất kỳ chuỗi thao tác hợp lệ nào luôn được giữ ở mức ổn định là O(1).
    pass


# --- BÀI 14
class BoDemHitCuaSoThoiGian:
    def __init__(self, t_giay):
        self.t_giay = t_giay
        self.hang_doi_thoi_gian = deque()

    def hit(self, thoi_diem_hien_tai):
        # Nhận một sự kiện xảy ra tại mốc thời gian `thoi_diem_hien_tai` (tính bằng giây)
        self.hang_doi_thoi_gian.append(thoi_diem_hien_tai)
        self._loai_bo_qua_han(thoi_diem_hien_tai)

    def _loai_bo_qua_han(self, thoi_diem_hien_tai):
        # Loại bỏ các phần tử đã vượt quá ngưỡng cửa sổ T giây ở đầu hàng đợi
        while self.hang_doi_thoi_gian and self.hang_doi_thoi_gian[0] <= thoi_diem_hien_tai - self.t_giay:
            self.hang_doi_thoi_gian.popleft()

    def lay_so_luong_hit(self, thoi_diem_hien_tai):
        self._loai_bo_qua_han(thoi_diem_hien_tai)
        return len(self.hang_doi_thoi_gian)

bo_dem = BoDemHitCuaSoThoiGian(300)  # Cửa sổ quét trong vòng 300 giây gần nhất
bo_dem.hit(10)
bo_dem.hit(150)
bo_dem.hit(305)
print("Bai 14 (So hit tai giay thu 310): ", bo_dem.lay_so_luong_hit(310))


# --- BÀI 15
def lap_lich_round_robin(cac_tien_trinh, quantum):
    # cac_tien_trinh: định dạng danh sách [["Tên", thời_gian_chạy], ...]
    hang_doi = deque(cac_tien_trinh)
    thoi_gian_he_thong = 0
    thoi_diem_hoan_thanh = {}
    
    while hang_doi:
        ten, thoi_gian_con_lai = hang_doi.popleft()
        
        if thoi_gian_con_lai <= quantum:
            thoi_gian_he_thong += thoi_gian_con_lai
            thoi_diem_hoan_thanh[ten] = thoi_gian_he_thong
        else:
            thoi_gian_he_thong += quantum
            hang_doi.append([ten, thoi_gian_con_lai - quantum])
            
    return thoi_diem_hoan_thanh

ds_tien_trinh = [["P1", 5], ["P2", 2], ["P3", 4]]
print("Bai 15 (Completion time): ", lap_lich_round_robin(ds_tien_trinh, 2))