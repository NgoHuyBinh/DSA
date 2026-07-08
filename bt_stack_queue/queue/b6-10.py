from collections import deque

# --- BÀI 6
class HangDoiBangHaiStack:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, x):
        self.in_stack.append(x)

    def dequeue(self):
        # Nếu out_stack rỗng, đổ toàn bộ phần tử từ in_stack sang
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        
        if not self.out_stack:
            return None  # Hàng đợi rỗng
        return self.out_stack.pop()

q6 = HangDoiBangHaiStack()
q6.enqueue(1)
q6.enqueue(2)
print("Bai 6: ", q6.dequeue())


# --- BÀI 7
def dao_nguoc_hang_doi(q):
    ngan_xep = []
    # Bước 1: Đẩy tất cả phần tử từ queue vào stack
    while q:
        ngan_xep.append(q.popleft())
    # Bước 2: Đẩy ngược lại từ stack vào queue
    while ngan_xep:
        q.append(ngan_xep.pop())
    return q

q7 = deque([1, 2, 3])
print("Bai 7: ", list(dao_nguoc_hang_doi(q7)))


# --- BÀI 8
class DequeCoBan:
    def __init__(self):
        self.mang = []

    def pushFront(self, x):
        self.mang.insert(0, x)

    def pushBack(self, x):
        self.mang.append(x)

    def popFront(self):
        if not self.mang:
            return None
        return self.mang.pop(0)

    def popBack(self):
        if not self.mang:
            return None
        return self.mang.pop()

dq8 = DequeCoBan()
dq8.pushFront(1)
dq8.pushBack(2)
print("Bai 8: ", dq8.mang)


# --- BÀI 9
def bfs_duyet_do_thi(do_thi, nut_nguon):
    da_tham = set([nut_nguon])
    hang_doi = deque([nut_nguon])
    thu_tu_tham = []
    
    while hang_doi:
        u = hang_doi.popleft()
        thu_tu_tham.append(u)
        
        for ke in do_thi.get(u, []):
            if ke not in da_tham:
                da_tham.add(ke)
                hang_doi.append(ke)
                
    return thu_tu_tham

# Đồ thị biểu diễn bằng danh sách kề
do_thi_mau = {
    1: [2, 3],
    2: [4],
    3: [4],
    4: []
}
print("Bai 9: ", bfs_duyet_do_thi(do_thi_mau, 1))


# --- BÀI 10
class PriorityQueueCoBan:
    def __init__(self):
        self.mang = []

    def push(self, x):
        # Chèn giữ thứ tự tăng dần để phần tử có ưu tiên cao nhất (nhỏ nhất) nằm ở cuối mảng
        idx = 0
        while idx < len(self.mang) and self.mang[idx] > x:
            idx += 1
        self.mang.insert(idx, x)

    def pop(self):
        if not self.mang:
            return None
        return self.mang.pop()  # Lấy ra phần tử nhỏ nhất trong O(1)

pq10 = PriorityQueueCoBan()
pq10.push(3)
pq10.push(1)
pq10.push(2)
print("Bai 10: ", pq10.pop())