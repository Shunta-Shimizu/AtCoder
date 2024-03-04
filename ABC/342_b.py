from collections import defaultdict
n = int(input())
P = list(map(int, input().split()))
q = int(input())
idx = defaultdict(int)
for i, p in enumerate(P):
    idx[p] = i

ans = []
for _ in range(q):
    a, b = map(int, input().split())
    if  idx[a] <= idx[b]:
        ans.append(a)
    else:
        ans.append(b)

for a in ans:
    print(a)