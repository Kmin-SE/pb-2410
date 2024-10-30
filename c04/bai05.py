def xin_chao(ten, nam_sinh):
    print(f'Xin chào, mình tên là {ten}.')
    print(f'Mình sinh năm {nam_sinh}.') 
    print('Rất vui được gặp bạn.')
    tuoi = 2024 - nam_sinh
    return tuoi

def nhap_ten():
    # Khi nhập sai thì cho nhập lại, nhập đúng thì dừng và trả về
    ten = input('Nhap ten: ')
    while ten == '':
        ten = input('Nhap ten: ')
    return ten

def nhap_ten_2():
    ten = ''
    while True:
        ten = input('Nhap ten: ')
        if ten != '':
            break
    return ten

def nhap_ten_3():
    ten = ''
    while True:
        ten = input('Nhap ten: ')
        if ten != '':
            return ten

def nhap_ten_4():
    ten = None
    while True:
        ten = input('Nhap ten (nhập x để dừng): ')
        if ten != '' and ten != 'x':
            return ten
        elif ten == 'x':
            break
    return ten
    

def nhap_nam_sinh():
    nam_sinh = int(input('Nhap nam sinh: '))
    while nam_sinh <= 1900:
         nam_sinh = int(input('Nhap nam sinh: '))
    return nam_sinh

def cn_xin_chao():
    ten = nhap_ten()
    nam_sinh = nhap_nam_sinh()
    t = xin_chao(ten, nam_sinh)
    print(t)

cn_xin_chao()



