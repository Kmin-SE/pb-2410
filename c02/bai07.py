# Cho nhập vào 3 số nguyên. Hãy in ra màn hình các số âm.

a = int(input("Nhap vao so thu nhat: "))
b = int(input("Nhap vao so thu hai: "))
c = int(input("Nhap vao so thu ba: "))

s = 0
if a < 0:
    s += a
if b < 0:
    s += b
if c < 0:
    s += c

print('tong:', s)

# bug
