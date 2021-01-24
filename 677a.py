a, b = map(int, input().split())
x = list(map(int, input().split()))
c = 0
for i in x:
    if i <= b:
        c += 1
    else:
        c += 2
print(c)
