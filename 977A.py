n, k = map(int, input().split())
while k:
    k -= 1
    if n % 10 == 0:
        n = str(n)
        n = int(n[:-1])
    else:
        n -= 1
print(n)
