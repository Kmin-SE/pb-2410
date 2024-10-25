n = 4
s = 0
# range(start, end): start -> end-1
for i in range(1, n+1):
    if i % 2 == 1:
        s += i
print(s)

# i = 1 => s = 1
# i = 2 => s = 1
# i = 3 => s = 4
# i = 4 => s = 4
