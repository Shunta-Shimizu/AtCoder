import math
r, x, y = map(int,input().split())

c = math.sqrt(x**2 + y**2)
if c < r:
    ans = 2
else:
    if c % r == 0:
        ans = int(c // r)
    else:
        ans = int(c // r) + 1
    
print(ans)

