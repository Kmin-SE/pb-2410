# Viết hàm nhập vào một mảng số nguyên.
def nhap_mang():
    arr = []
    # Nhập số lượng phần tử:
    n = int(input("Nhap so luong phan tu: "))

    # Nhập từng phần tử
    for i in range(n):
        value = int(input("Nhap phan tu: "))
        arr.append(value)

    return arr

# Liệt kê các số dương trong mảng một chiều số nguyên.
def liet_ke_duong(arr):
    for value in arr:
        if value > 0:
            print(value)

def loc_duong(arr):
    res = []
    for value in arr:
        if value > 0:
            res.append(value)
    return res

# Đếm các số lẻ trong mảng một chiều số nguyên.
def dem_le(arr):
    count = 0
    for value in arr:
        if value % 2 == 1:
            count += 1
    return count

# Tính tổng các số âm trong mảng một chiều số nguyên.
def tong_am(arr):
    sum = 0
    for value in arr:
        if value < 0:
            sum += value
    return sum

# Tìm giá trị âm đầu tiên trong mảng một chiều số nguyên. 
def tim_am_dau(arr):
    am_dau = 0
    for value in arr:
        if value < 0:
            am_dau = value
            break
    return am_dau

def tim_am_dau_2(arr):
    for value in arr:
        if value < 0:
            return value
    return 0 # Khong co


# Cho trước một mảng lưu các mã số sinh viên. 
# Cho phép nhập vào một mã số. Hãy cho biết mã số này xuất hiện ở đâu trong mảng.
def tim_vt(arr, key):
    n = len(arr)
    vt = -1
    for i in range(n):
        if arr[i] == key:
            vt = i
            break
    return vt

def tim_vt_2(arr, key):
    n = len(arr)
    for i in range(n):
        if arr[i] == key:
            return i
    return -1 # Khong co

def tim_vt_3(arr, key):
    res = []
    n = len(arr)
    for i in range(n):
        if arr[i] == key:
            res.append(i)
    return res
    
# Tìm số lớn nhất trong danh sách các số nguyên (lính canh)
def tim_max(arr):
    max = arr[0]
    for value in arr:
        if value > max:
            max = value
    return max



# Tìm số âm lớn nhất trong danh sách các số nguyên
def tim_max_am(arr):
    max = tim_am_dau(arr)

    for value in arr:
        if value < 0 and value > max:
            max = value
    return max

# Hãy cho biết trong mảng có phải toàn là số âm không.
def kt_toan_am(arr):
    flag = True
    for value in arr:
        if value >= 0:
            flag = False
            break
    return flag

def kt_toan_am_2(arr):
    for value in arr:
        if value >= 0:
            return False    
    return True

a = nhap_mang()
print(kt_toan_am(a))


# max_am = tim_max_am(a)
# if max_am == 0:
#     print('Khong co so am')
# else:
#     print('So am lon nhat:', max_am)

# print(tim_max(a))

# a = nhap_mang()
# print(tim_vt_3(a, 3))

# a = nhap_mang()
# r = tim_am_dau(a)
# if r == 0:
#     print('Khong co so am')
# else:
#     print('So am dau la:', r)