'''
- co 3 loi thuong gap:
1. loi cu phap (syntax errors)
2. loi thuc thi (run-time exceptions)
3. loi nghiep vu (logic errors)
--> su dung try...catch
'''

try:
    x = 5
    y = 0
    z = x/y
    print(z)
except:
    print("Error")