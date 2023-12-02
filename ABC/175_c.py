x, k, d = map(int, input().split())

if x >= 0:
    if k <= (x // d):
        ans = abs(x - k*d)
    else:
        if (k-(x//d)) % 2 == 0:
            ans = abs(x - (x//d) * d)
        else:
            ans = abs(x - (x//d+1) * d)

else:
    if k <= (abs(x) // d):
        ans = abs(x + k*d)
    else:
        if (k-(abs(x)//d)) % 2 == 0:
            ans = abs(x + (abs(x)//d) * d)
        else:
            ans = abs(x + (abs(x)//d+1) * d)

print(ans)

