# Hàm in ra lời chào 
# ten (string): tên của một người
# nam_sinh (int): năm sinh của một người
def xin_chao(ten, nam_sinh=2000):
    print(f'Xin chào, mình tên là {ten}.')
    print(f'Mình sinh năm {nam_sinh}.') 
    print('Rất vui được gặp bạn.')

# xin_chao(nam_sinh=2016, ten='Kmin')
# xin_chao('Hieu', 2008)
xin_chao('Kmin')