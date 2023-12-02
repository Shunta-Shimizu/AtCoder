from collections import defaultdict
n, k = map(int, input().split())
C = list(map(int, input().split()))

if n == k:
    print(len(set(C)))
    exit()

kind = defaultdict(int)
ans = 0
num = 0
for i in range(n):
    if kind[C[i]] == 0:
        num += 1
    kind[C[i]] += 1
    if i >= k:
        kind[C[i-k]] -= 1
        if kind[C[i-k]] == 0:
            num -= 1
    ans = max(ans, num)

print(ans)

