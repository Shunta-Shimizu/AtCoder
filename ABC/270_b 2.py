x ,y, z = map(int, input().split())

if y < 0:
    x = x*(-1)
    y = y*(-1)
    z = z*(-1)

if x < y:
    print(abs(x))
else:
    if z < y:
        print(abs(z)+abs(x-z))
    else:
        print(-1)

