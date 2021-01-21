for i in range(int(input())):
    a = input()
    print(a[0] + str(len(a) - 2) + a[-1] if len(a) > 10 else a)
