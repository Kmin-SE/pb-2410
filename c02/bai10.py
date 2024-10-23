# Cho phép nhập vào năm sinh, chiều cao và cân nặng của một người. Nếu người này từ 18 tuổi trở lên,
# chương trình sẽ tính chỉ số BMI, in chỉ số này ra và đưa ra đánh giá cho người dùng biết. Ngược lại, nếu
# người dùng này dưới 18 tuổi, chương trình thông báo “Không khả dụng”.

namSinh = int(input("Nhập năm sinh của bạn: "))
height = float(input("Nhập vào chiều cao của bạn (m) vidu: 1.71 (là 1m71): "))
weight = float(input("Nhập cân nặng: "))

if 2024 - namSinh >= 18:
    bmi = weight/(height**2)
    print("Chỉ số BMI của bạn là: ", bmi)
    if bmi < 18.5:
        print("Bạn Gầy")
    elif bmi < 25:
        print("Bạn Bình thường")
    elif bmi < 30:
        print("Bạn Thừa cân")
    else:
        print("Bạn Béo phì")
else:
    print("Không khả dụng")