from collections import defaultdict
n, m = map(int, input().split())
H = list(map(int, input().split()))

AB = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    AB[a].append(H[b-1])
    AB[b].append(H[a-1])

tf = [True for _ in range(n)]
for k, ab in AB.items():
    if H[k-1] <= max(ab):
        tf[k-1] = False

ans = 0
for i in range(n):
    if tf[i]:
        ans += 1

print(ans)
