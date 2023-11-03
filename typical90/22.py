import math
a, b, c = map(int, input().split())

r = math.gcd(a, math.gcd(b, c))
ans = (a//r-1)+(b//r-1)+(c//r-1)
print(ans)