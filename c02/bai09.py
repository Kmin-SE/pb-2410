# Cho nhập vào một tháng trong năm nay. Hãy cho biết tháng đó có
# bao nhiêu ngày.
# Giả sử nhập vào thang = 1


# nam = 2024
# thang = int(input("Nhap vao thang: "))
# if thang == 2:
#     print("Thang nay co 29 ngay")
# elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
#     print("Thang nay co 30 ngay")
# else:
#     print("Thang nay co 31 ngay")

month = int(input("Nhập tháng"))
if month in [1, 3, 5, 7, 8, 10, 12]: # ktra month == 1, month == 3,...
    print("có 31 ngày")
elif month in [4,6,9,11]:
    print("Có 30 ngày")
else:
    print ("có 29 ngày")