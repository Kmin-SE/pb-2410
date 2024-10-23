# k = 1 => "* "
# k = 2 => "* *"
# k = 3 => "* * *"

k = 5
s = ""
i = 1
while i <= k:
    s += "* "
    i += 1

print(s)