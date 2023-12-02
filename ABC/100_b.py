d, n = map(int, input().split())

if d == 0:
    if n == 100:
        n += 100**d
    print(n)
else:
    if n == 100:
        print(n*100**d+100**d)
    else:
        print(n*100**d)
