a, b = map(int, input().split())


if a <= b:
    print(1)
else:
    if a % b == 0:
        print(a//b)
    else:
        print(a//b+1)