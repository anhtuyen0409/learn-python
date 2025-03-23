# 1. kiểu int (kiểu số nguyên)
# 2. kiểu float (kiểu số thực)
# 3. kiểu complex (kiểu số phức)
# vd: z = 2 + 3j (2 là phần thực, 3 là phần ảo); z = complex(2,3) -> 2 la phần thực, 3 là phần ảo
# 4. kiểu str (kiểu chuỗi): có thể viết nháy đơn hoặc đôi
# vd: "hello", 'hi'
# 5. kiểu bool (True/False)
# khai báo biến: Python không cần khai báo kiểu dữ liệu, khi gán giá trị thì python tự động suy ra kiểu dữ liệu -> như vậy 1 biến có thể có nhiều kiểu dữ liệu tuỳ thuộc vào giá trị ta gán
# có thể dùng hàm Type() để kiểm tra kiểu dữ liệu
# cách xoá biến: nếu biến đó đang tồn tại mà ta xoá nó đi thì không còn sử dụng được nữa (tương tự C++ khi thu hồi bộ nhớ con trỏ), python dùng từ khoá del để xoá
# cách kiểm tra vùng lưu trữ -> import thư viện sys

x = 2
print(type(x))
x = 2.5
print(type(x))
x = 'hello'
print(type(x))
x = True
print(type(x))
x = complex(2,5)
print(type(x))
print("phan thuc: ", x.real, "phan ao: ", x.imag)