n = int(input())
c = 0
while n:
    n -= 1
    a = input()
    if a == "Tetrahedron":
        c += 4
    elif a == "Cube":
        c += 6
    elif a == "Octahedron":
        c += 8
    elif a == "Dodecahedron":
        c += 12
    elif a == "Icosahedron":
        c += 20

print(c)
