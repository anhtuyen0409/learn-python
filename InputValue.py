'''
- để nhop dữ lệu tu bàn phím, ta dùng hàm input()
- giá trị nhập vào cua hàm input() thường là kiểu chuỗi, do đó cần phải chuyển kiểu neu như muốn lưu trữ giá trị nhập vào không phải kiểu chuôi

'''

print("Mời nhập giá trị: ")
s = input()
print("Giá trị bạn đã nhap: ",s)
print(type(s))

print("Mời nhập giá trị số: ")
s = int(input()) # chuyển kiểu int
print("Giá trị bạn đã nhap: ",s)
print(type(s))

def strToBool(s) :
    return s.lower() in ("true", "t", "1", "yes")
x = input("Moi nhap True/False: ")
x = strToBool(x)
print(x)