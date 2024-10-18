diem_tb = float(input("Nhap vao diem trung binh toan khoa hoc: "))
if diem_tb >= 5.0:
    print("Sinh vien tot nghiep")
    if diem_tb >= 8.0:
        print("Duoc loai gioi")
    elif diem_tb >= 6.5:
        print("Duoc loai kha")
    else:
        print("Duoc loai trung binh")
else:
    print("Sinh vien truot tot nghiep")


diem_tb = float(input("Nhap vao diem trung binh toan khoa hoc: "))

kq = ""

if diem_tb >= 5.0:
    kq = "Sinh vien tot nghiep va "
    if diem_tb >= 8.0:
        kq += "duoc loai gioi"
    elif diem_tb >= 6.5:
        kq += "duoc loai kha"
    else:
        kq += "duoc loai trung binh"
else:
    kq = "Sinh vien truot tot nghiep"

print(kq)