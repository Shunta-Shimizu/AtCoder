import math
n = int(input())

ans = 10 ** 12
for i in range(1, int(math.sqrt(n))+1):
    if n % i == 0:
        count = i-1+(n//i-1)
        ans = min(count, ans)

print(ans)