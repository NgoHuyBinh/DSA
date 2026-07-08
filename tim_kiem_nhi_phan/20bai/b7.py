def ton_tai(a, x):
    for element in a:
        if element == x:
            return True 
    return False 

mang_so = [1, 5, 9, 12, 45, 3]
print(ton_tai(mang_so, 9))   
print(ton_tai(mang_so, 10))  

mang_chuoi = ["apple", "banana", "orange"]
print(ton_tai(mang_chuoi, "banana")) 
print(ton_tai(mang_chuoi, "grape"))  