# Biến chạy: i chạy theo quy luật nào? [a, b] (kèm bước nhảy)
# Với mỗi lần lặp (với mỗi i): làm việc gì?

# In các 5 số nguyên trong đoạn [1, n]
# Biến chạy i chạy [1, n] (+1)
# Với mỗi i: In i

n = 9

i = 1
while i <= n:
    print(i)
    i = i + 1

# Hình dung:
# i = 1 2 3


n = 9

i = 1
while i <= n:
    print(i)
    i = i + 2

# i chạy [1, 9] (+2)
# 1 3 7 9


n = 9

i = 1
while i <= n:
    print(i*2)
    i = i + 2

# 2 6