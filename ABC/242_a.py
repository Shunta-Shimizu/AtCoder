a, b, c, x = map(int, input().split())

if a < x <= b:
    p = c / (b - a)
    if p >= 1:
        p = 1
    print(p)
elif x <= a:
    print(1)
else:
    print(0)
