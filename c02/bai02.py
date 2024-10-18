# Cho 3 cạnh của một tam giác. 
# Hãy kiểm tra tam giác này có phải tam giác đều hay không.

# Input: 3 cạnh (3 số thực)
# Output: Có đều / Không đều

# Nhập 3 cạnh a, b, c

# Nếu a, b, c bằng nhau thì có, ngược lại thì không

# canhA = float(input("Nhập cạnh A của tam giác: "))
# canhB = float(input("Nhập cạnh B của tam giác: "))
# canhC = float(input("Nhập cạnh C của tam giác: "))
# if canhA == canhB and canhB == canhC :
#     print("Là tam giác đều")
# else:    
#     print("Không phải tam giác đều")

a = float(input("Nhap vao canh thu nhat: "))
b = float(input("Nhap vao canh thu hai: "))
c = float(input("Nhap vao canh thu ba: "))
if a == b == c:
    print ("tam giac nay la tam giac deu")
else:
    print ("tam giac nay khong phai la tam giac deu")


