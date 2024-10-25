# Tìm số đầu tiên chia hết cho 6

m = 1
n = 20
for i in range(m, n+1):
    if i % 6 == 0:
        print(i)
        break