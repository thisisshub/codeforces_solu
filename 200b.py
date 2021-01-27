n = int(input())
a = list(map(int, input().split()))
c = 0
for i in range(n):
    c += a[i] / 100
print(c / n * 100)
