def xin_chao(ten, nam_sinh):
    print(f'Xin chào, mình tên là {ten}.')
    print(f'Mình sinh năm {nam_sinh}.') 
    print('Rất vui được gặp bạn.')
    tuoi = 2024 - nam_sinh
    return tuoi

def cn_xin_chao():
    ten = input('Nhap ten: ')
    nam_sinh = int(input('Nhap nam sinh: '))
    t = xin_chao(ten, nam_sinh)
    print(t)

cn_xin_chao()



