import math
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False 
    return True  
def tim_snt_dau_tien(a):
    for i in range(len(a)):
        if la_so_nguyen_to(a[i]):
            return a[i], i  
    return None, -1
mang_1 = [4, 6, 9, 7, 10]
gia_tri, vi_tri = tim_snt_dau_tien(mang_1)
print(f"Mảng xét: {mang_1}")
print(f"Số nguyên tố đầu tiên là {gia_tri} tại vị trí {vi_tri}")
