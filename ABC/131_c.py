import math
a, b, c, d = map(int, input().split())

def lcm(n, m):
    return n*m // math.gcd(n, m)

c_div = b // c - a // c
d_div = b // d - a // d
cd_div = b // lcm(c, d) - a // lcm(c, d)

if a % c == 0:
    c_div += 1
if a % d == 0:
    d_div += 1
if a % lcm(c, d) == 0:
    cd_div += 1

ans = b-a+1 - (c_div+d_div-cd_div)
print(ans)