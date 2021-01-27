n = int(input())
a = list(map(int, input().split()))
print("HARD" if sum(a) != 0 else "EASY")
