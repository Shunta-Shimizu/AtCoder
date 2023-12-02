x, a, d, n = map(int, input().split())

if d == 0:
    print(abs(a-x))
    exit()

if d < 0:
    a = a + d * (n-1)
    d = -d

i = (x - a) // d

def check_i(i):
    if i < 0:
        i = 0
    elif i > n-1:
        i = n-1
    return i

ans = abs(a + d * check_i(i) - x)
ans = min(ans, abs(a + d * check_i(i+1) - x))
print(ans)



