from collections import defaultdict
n, k = map(int, input().split())
A = list(map(int, input().split()))

tf = defaultdict(bool)
ans = (1+k)*k//2
for a in A:
    if a > k:
        continue
    else:
        if not tf[a]:
            tf[a] = True
            ans -= a

print(ans)