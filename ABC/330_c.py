import math
d = int(input())

ans = 10**10
y = int(math.sqrt(d)+2)
for x in range(int(math.sqrt(d)+2)):
    while y > 0 and x**2+y**2 > d:
        y -= 1
    ans = min(ans, abs(x**2+y**2-d))
    ans = min(ans, abs(x**2+(y+1)**2-d))

print(ans)


