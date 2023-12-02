l, r = map(int, input().split())

if r-l >= 2019:
    lmod = 0
    rmod = 2018
else:
    lmod = l % 2019
    rmod = r % 2019

ans = 10**10
for i in range(2019):
    for j in range(2019):
        if lmod <= i < j <= rmod:
            ans = min(ans, (i*j)%2019)

print(ans)