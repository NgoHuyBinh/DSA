from collections import deque

# --- BÀI 1
class HangDoiCoBan:
    def __init__(self):
        self.hang_doi = deque()

    def enqueue(self, x):
        self.hang_doi.append(x)

    def dequeue(self):
        if self.isEmpty():
            return None
        return self.hang_doi.popleft()

    def front(self):
        if self.isEmpty():
            return None
        return self.hang_doi[0]

    def isEmpty(self):
        return len(self.hang_doi) == 0

q1 = HangDoiCoBan()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
print("Bai 1: ", q1.dequeue())


# --- BÀI 2
class CircularQueue:
    def __init__(self, dung_luong):
        self.dung_luong = dung_luong
        self.mang = [None] * dung_luong
        self.dau = -1  # front
        self.cuoi = -1  # rear

    def enqueue(self, x):
        if (self.cuoi + 1) % self.dung_luong == self.dau:
            return False  # Hàng đợi đầy
        elif self.dau == -1:
            self.dau = 0
            self.cuoi = 0
        else:
            self.cuoi = (self.cuoi + 1) % self.dung_luong
        self.mang[self.cuoi] = x
        return True

    def dequeue(self):
        if self.dau == -1:
            return None  # Hàng đợi rỗng
        gia_tri_tra_ve = self.mang[self.dau]
        if self.dau == self.cuoi:
            self.dau = -1
            self.cuoi = -1
        else:
            self.dau = (self.dau + 1) % self.dung_luong
        return gia_tri_tra_ve

q2 = CircularQueue(4)
q2.enqueue(10)
print("Bai 2: ", q2.dequeue())


# --- BÀI 3
def mo_phong_day_thao_tac(thao_tac):
    q = deque()
    ket_qua_deq = []
    
    for lenh in thao_tac:
        if lenh.startswith("enq"):
            _, gia_tri = lenh.split()
            q.append(int(gia_tri))
        elif lenh == "deq":
            if q:
                ket_qua_deq.append(q.popleft())
                
    print("Bai 3: Gia tri dequeue:", ket_qua_deq, "| Trang thai cuoi:", list(q))

mo_phong_day_thao_tac(["enq 5", "enq 7", "deq"])


# --- BÀI 4
class HangDoiKiemTraDungLuong:
    def __init__(self, dung_luong):
        self.dung_luong = dung_luong
        self.mang = [None] * dung_luong
        self.dau = -1
        self.cuoi = -1
        self.so_luong = 0

    def isFull(self):
        return self.so_luong == self.dung_luong

    def isEmpty(self):
        return self.so_luong == 0

    def enqueue(self, x):
        if self.isFull():
            print("Loi: Enqueue loi vi hang doi da day!")
            return False
        if self.isEmpty():
            self.dau = 0
            self.cuoi = 0
        else:
            self.cuoi = (self.cuoi + 1) % self.dung_luong
        self.mang[self.cuoi] = x
        self.so_luong += 1
        return True

    def dequeue(self):
        if self.isEmpty():
            print("Loi: Dequeue loi vi hang doi dang rong!")
            return None
        gia_tri = self.mang[self.dau]
        self.so_luong -= 1
        if self.isEmpty():
            self.dau = -1
            self.cuoi = -1
        else:
            self.dau = (self.dau + 1) % self.dung_luong
        return gia_tri

    def dem_phan_tu(self):
        return self.so_luong

q4 = HangDoiKiemTraDungLuong(2)
q4.dequeue()  # Gây lỗi rỗng


# --- BÀI 5
class HangDoiXemDauCuoi:
    def __init__(self):
        self.mang = []

    def enqueue(self, x):
        self.mang.append(x)

    def dequeue(self):
        if not self.mang:
            return None
        return self.mang.pop(0)

    def get_front(self):
        if not self.mang:
            return None
        return self.mang[0]

    def get_rear(self):
        if not self.mang:
            return None
        return self.mang[-1]

q5 = HangDoiXemDauCuoi()
q5.enqueue(4)
q5.enqueue(5)
q5.enqueue(6)
print(f"Bai 5: front={q5.get_front()}, rear={q5.get_rear()}")