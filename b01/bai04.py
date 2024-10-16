# Hãy viết chương trình khai báo một biến dùng để 
# lưu năm sinh của 3 người bạn. 
# Hãy tính tuổi trung bình của họ.

# Thuật toán (algorithm)

# Bước 1: Khai báo biến ds_nam_sinh để lưu 3 số
ds_nam_sinh = [2001, 2002, 2003]

# Bước 2: Tính tuổi của từng bạn
tuoi_a = 2024 - ds_nam_sinh[0]
tuoi_b = 2024 - ds_nam_sinh[1]
tuoi_c = 2024 - ds_nam_sinh[2]
# tuoi = [2024 - ds_nam_sinh[0], 2024 - ds_nam_sinh[1], 2024 - ds_nam_sinh[2]]

# Bước 3: Tính trung bình tuổi
tuoi_tb = (tuoi_a + tuoi_b + tuoi_c) / 3

# Bước 4: In tuổi trung bình
print('Tuoi trung binh:', tuoi_tb)
