n = input()
x = y = 0
for i in n:
    if i.isupper():
        x += 1
    else:
        y += 1

print(n.upper() if x > y else n.lower())
