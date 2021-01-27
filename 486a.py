from sys import stdin, stdout

n = int(stdin.readline())
stdout.write(str(n // 2 if n % 2 == 0 else -(n + 1) // 2))
