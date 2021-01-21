c = 0
for i in range(int(input())):
    a = list(map(int, input().split()))
    if sum(a) >= 2:
        c += 1
print(c)
