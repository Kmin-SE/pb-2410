# Hãy vẽ ra màn hình một đoạn thẳng có độ dài k, có quy luật xen kẽ 
# * $ * $ * $, k được nhập từ bàn phím.

k = 6
s = ""
for i in range(k):
    if i % 2 == 0:
        s += "* "
    else:
        s += "$ "
    print(s)

print(s)

# bug
# debug
# fix bug

# IDE = Integrated Development Environment (VS Code, VS, PyCharm, ...)
 