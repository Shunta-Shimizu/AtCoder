import math
def solve(x):
    res = 0
    for i in range(1, int(math.sqrt(x))+1):
        if x % i != 0:
            continue
        else:
            j = x // i
            if i == j:
                res += 1
            else:
                res += 2
    
    return res

n = int(input())

ans = 0
for x in range(1, n):
    y = n-x
    ans += solve(x) * solve(y)

print(ans)