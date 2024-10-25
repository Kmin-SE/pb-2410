# Cho trước một số nguyên n. Hãy in ra màn các ước số của n.

# a là ước của b nếu b chia hết cho a
# vd: ước của 6 là: 1, 2, 3, 6
# domain knowledge

# input: n
# output: các ước của n

# i [start, end, step] => [1, n, 1]
# Làm gì ở mỗi i => Nếu n chia hết cho i thì i là ước của n

n = 6
for i in range(1, n+1):
    if n % i == 0:
        print(i)







