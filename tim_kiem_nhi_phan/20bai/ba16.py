def phan_tu_gan_x_nhat(a, x):
    if len(a) == 0:
        return None, -1
    gan_nhat = a[0]
    vi_tri_gan_nhat = 0
    chenh_lech_min = abs(a[0] - x)
    for i in range(1, len(a)):
        chenh_lech_hien_tai = abs(a[i] - x)
        if chenh_lech_hien_tai < chenh_lech_min:
            chenh_lech_min = chenh_lech_hien_tai
            gan_nhat = a[i]
            vi_tri_gan_nhat = i
    return gan_nhat, vi_tri_gan_nhat
mang_so = [10, 22, 28, 29, 40]
x = 26

gia_tri, vi_tri = phan_tu_gan_x_nhat(mang_so, x)
print(f"Mảng xét: {mang_so}, x = {x}")
print(f"Phần tử gần {x} nhất là: {gia_tri} tại vị trí {vi_tri}")