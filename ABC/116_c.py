from collections import defaultdict
n = int(input())
H = list(map(int, input().split()))

ans = 0
count = 0
for i in range(n):
    if count >= H[i]:
        count = H[i]
    else:
        ans += H[i]-count
        count = H[i]

print(ans)