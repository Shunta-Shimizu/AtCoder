n, a, b = map(int, input().split())

for i in range(n):
    x = ""
    for j in range(n):
        if i % 2 == 0 and j % 2 == 0:
            x += "." * b
        elif i % 2 == 0 and j % 2 != 0:
            x += "#" * b
        elif i % 2 != 0 and j % 2 == 0:
            x += "#" * b
        elif i % 2 != 0 and j % 2 != 0:
            x += "." * b
    
    for _ in range(a):
        print(x)

