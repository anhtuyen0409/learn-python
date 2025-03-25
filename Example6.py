year = int(input("Nhap nam: "))
if(year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Nam ",year, " la nam nhuan")
else:
    print("Nam ",year," khong nhuan")