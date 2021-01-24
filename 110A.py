n = input()
c = set(str(n.count("4") + n.count("7")))
print("YES" if c == {"4", "7"} or c == {"4"} or c == {"7"} else "NO")
