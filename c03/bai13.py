# n = 5
# flag = False
# for i in range(2, n):
#     if n % i == 0:
#         flag = True
#         break

# if flag == True:
#     print("Co")
# else:
#     print("Khong")

n = 5
flag = 0
for i in range(2, n):
    if n % i == 0:
        flag = 1
        break

if flag == 1:
    print("Co")
else:
    print("Khong")

n = 5
flag = 4
for i in range(2, n):
    if n % i == 0:
        flag = 9
        break

if flag == 9:
    print("Co")
else:
    print("Khong")