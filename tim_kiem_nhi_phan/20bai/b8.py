def dem_x(a, x):
    dem_so = 0 
    for i in a:
        if i == x:
            dem_so += 1  
    return dem_so 

mang_so = [1, 2, 3, 4, 5, 6, 7, 8, 1, 5]
x = int(input("Nhập vào số x để xét: "))

ket_qua = dem_x(mang_so, x)
print("Số lần xuất hiện của", x, "là:", ket_qua)