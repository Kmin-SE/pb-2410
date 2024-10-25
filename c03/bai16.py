# w = 7
# h = 5
# for j in range(h):
#     s = ""
#     if j == 0 or j == h-1:
#         for i in range(w):
#             s += "* "
#     else:
#         for i in range(w):
#             if i == 0 or i == w-1:
#                 s += "* "
#             else:
#                 s += "  "
#     print(s)

w = 7
h = 5
for j in range(h):
    s = ""
    for i in range(w):
        if j == 0 or j == h-1 or i == 0 or i == w-1:
            s += "* "
        else:
            s += "  "
    print(s)