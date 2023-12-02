n = int(input())

A = []
P = []
X = []
for _ in range(n):
    a, p, x = map(int, input().split())
    A.append(a)
    P.append(p)
    X.append(x)

ans = set()
t = 0
res = 0
for i in range(n):
    t = A[i]
    res = X[i] - t 
    if res <= 0:
        ans.add(-1)
    else:
        ans.add(P[i])

if len(ans) == 1 and -1 in ans:
    print(-1)
else:
    ans = sorted(list(ans))
    print(ans[1])

    