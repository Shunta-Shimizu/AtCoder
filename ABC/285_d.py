import math

n = int(input())
A = list(map(int, input().split()))

if n == 1:
    lcm_n = A[0]
    ans = lcm_n
else:
    lcm_n = A[0]
    for i in range(1, n):
        lcm_n = math.lcm(lcm_n, A[i])
    s = 0
    b = lcm_n
    for i in range(n):
        s += lcm_n//A[i]
    
    ans = b/s

print(ans)