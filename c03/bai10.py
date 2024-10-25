# Đếm xem có bao nhiêu số chẵn trong đoạn [m, n]
m = 1
n = 7

count = 0
for i in range(m, n+1):
    if i % 2 == 0:
        count += 1

print(count)