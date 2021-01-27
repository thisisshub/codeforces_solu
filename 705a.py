n = int(input())
a = ["I hate that ", "I love that "]
c = ""
for i in range(n):
    if i % 2 == 0:
        c += a[0]
    else:
        c += a[1]
print(c[: len(c) - 6] + " it")
