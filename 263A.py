l = []
for i in range(5):
    ll = list(map(int, input().split()))
    l.append(ll)
x = [(ix, iy) for ix, row in enumerate(l) for iy, i in enumerate(row) if i == 1]
c = 0
for i in x:
    for j in i:
        c += abs(j - 2)
print(c)
