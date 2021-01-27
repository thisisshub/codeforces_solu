a = input()
a = list(a)
b = input()
b = list(b)
l = []
for i in range(len(a)):
    if a[i] != b[i]:
        l.append("1")
    else:
        l.append("0")
print("".join(l))
