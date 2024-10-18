# Kiểm tra số nguyên x được nhập vào từ bàn phím 
# có phải là số âm không.

# # Nhập x
# x = int(input('Nhap x: '))

# # Nếu x âm thì in ra "Co". Ngược lại, in ra "Khong"
# if x < 0:
#     print('Co')
# else:
#     print('Khong')

# Nhập x
x = int(input('Nhap x: '))

# Nếu x âm thì in ra "Co". Ngược lại, in ra "Khong"
kq = ''
if x < 0:
    kq = 'Co'
else:
    kq = 'Khong'

# Xuất KQ
print(kq)