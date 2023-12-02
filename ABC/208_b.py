import math
p = int(input())

ans = 0
for i in range(10, 0, -1):
    while p >= math.factorial(i):
        p -= math.factorial(i)
        ans += 1

print(ans)

