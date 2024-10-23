# Cho nhập vào 3 số nguyên. Hãy in ra màn hình các số âm.

a = int(input("Nhap vao so thu nhat: "))
b = int(input("Nhap vao so thu hai: "))
c = int(input("Nhap vao so thu ba: "))

count = 0
if a < 0:
    count += 1
if b < 0:
    count += 1
if c < 0:
    count += 1

print('count:', count)

# bug
