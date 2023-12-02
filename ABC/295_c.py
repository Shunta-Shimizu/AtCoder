from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))

pair = defaultdict(int)
for i in range(n):
    pair[A[i]] += 1

ans = 0
for k, v in pair.items():
    if v > 1:
        ans += v // 2

print(ans)

