n, x, y, z = map(int, input().split())

if x <= z <= y:
    print("Yes")
elif y <= z <= x:
    print("Yes")
else:
    print("No")