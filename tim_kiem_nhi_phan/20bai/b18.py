def tim_kiem_ma_tran(M, x):
    so_dong = len(M)
    for r in range(so_dong):
        so_cot = len(M[r])
        for c in range(so_cot):
            if M[r][c] == x:
                return r, c 
    return -1, -1
M = [
    [5, 8, 1],
    [3, 9, 7],
    [2, 6, 4]
]
x = 9

dong, cot = tim_kiem_ma_tran(M, x)
print(f"Ma trận M: {M}")
print(f"Giá trị cần tìm x = {x}")
print(f"Vị trí (dòng, cột) đầu tiên tìm thấy là: ({dong}, {cot})")
