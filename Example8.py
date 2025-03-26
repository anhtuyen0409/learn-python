import math

a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))
if a==0:
    if b==0:
        if c==0:
            print("Phuong trinh co vo so nghiem")
        else:
            print("Phuong trinh vo nghiem")
    else:
        print("Phuong trinh co nghiem x = ",-c/b)
else:
    delta = b**2 - 4*a*c
    if delta>0:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print("Phuong trinh co 2 nghiem: x1 = ",x1,", x2 = ",x2)
    elif delta==0:
        print("Phuong trinh co nghiem kep: x = ",-b/2*a)
    else:
        print("Phuong trinh vo nghiem")