"""
1. toán tử số học (+,-,*,/ (chia lấy kết quả chính xác), // (chia lấy phần nguyên), % (chia lấy phần dư), ** (luỹ thừa))
2. toán tu gan (=, +=, -=, *=, /=, //=, %=, **=)
3. toán tử so sánh (==, !=, <, <=, >, >=, is (trả ve True neu cac bien ở 2 bên toán tử cùng trỏ tới 1 doi tượng (hoặc cùng giá trị), nếu không là False), is not)
4. toán tử logic (and, or, not)
"""

x = 3
y = x**2
print(y) # y = 9

year = 2025
t = year % 2 == 0 and year % 3 == 0
print(t) # False
t = year % 2 == 0 or year % 3 == 0
print(t) # True
print(5 is 5) # True
print(5 is not 5) # False
print(9/2) # 4.5
print(9//2) # 4
print(9%2) # 1