x, k = map(int, input().split())

for i in range(1, k+1):
    y = x // 10
    z = x % 10
    if z >= 5:
        y += 1
        x = y
    else:
        x = y


print(x*10**k)