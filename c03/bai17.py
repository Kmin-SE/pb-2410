a = 10
for j in range(2, a):
    count = 0
    for i in range(1, j+1):
        if j % i == 0:
            count += 1
    if count == 2: # j là SNT
        print(j)


# n = 7
# count = 0
# for i in range(1, n+1):
#     if n % i == 0:
#         count += 1
# if count == 2:
#     print("SNT")
# else:
#     print("Khong phai SNT")