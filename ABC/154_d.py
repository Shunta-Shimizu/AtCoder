from collections import deque
n, k = map(int, input().split())
P = list(map(int, input().split()))

A = []
for p in P:
    A.append((p+1)/2)

ans = 0
for i in range(k):
    ans += A[i]

pre = ans
for i, ap in enumerate(A[k:]):
    pre -= A[i]
    ans = max(ans, pre+ap)
    pre += ap

print(ans)