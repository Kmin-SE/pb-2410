
# Cho phép nhập vào một năm. Hãy cho biết năm đó có phải là năm
# nhuận hay không? Biết rằng: Năm nhuận là năm chia hết cho 4
# nhưng không chia hết cho 100 hoặc là năm chia hết cho 400. Quy
# ước: Yes/No


# Giả sử nhập vào nam = 2024




nam = int(input("Nhap vao nam: "))

if nam % 4 == 0 and nam % 100 != 0 or nam % 400 == 0:
    print ("Nam tren la nam nhuan")
else:
    print ("Nam tren la nam khong nhuan")