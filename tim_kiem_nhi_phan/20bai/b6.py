def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i  
    return -1  


if __name__ == "__main__":
    try:
        input_str = input("Nhập các phần tử của mảng cách nhau bằng khoảng trắng: ")
        a = [int(item) for item in input_str.split()]
        
        x = int(input("Nhập giá trị x cần tìm: "))

        result = linear_search(a, x)
        
        if result != -1:
            print(f"Tìm thấy {x} tại vị trí: {result}")
        else:
            print(f"Không tìm thấy {x} trong mảng. {result}")
            
    except ValueError:
        print("Vui lòng chỉ nhập các số nguyên hợp lệ!")