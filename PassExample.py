'''
- biểu thức pass dùng để dành code sau. Vi du khi biet chỗ đó viết rất nhiều code, nhưng tại thời điểm đó chưa kịp làm -> Ta dung Pass de danh dau vi tri do
'''

a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
if a==0:
    pass # đánh dấu để code sau
else:
    x = -b/a
    print("Nghiem x = ",x)