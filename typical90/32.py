import itertools
n = int(input())
A = []
for _ in range(n):
    a = list(map(int, input().split()))
    A.append(a)

m = int(input())
XY = set()
for _ in range(m):
    x, y = map(int, input().split())
    XY.add((x-1, y-1))
    XY.add((y-1, x-1))

RP = list(itertools.permutations([i for i in range(n)], n))
# print(RP)
ans = 10**8
for R in RP:
    t = 0
    tf = True
    for i, r in enumerate(R):
        if i == 0:
            now = r
            pre = -1
            t += A[r][i]
        else:
            pre = now
            now = r
            if (pre, now) in XY or (now, pre) in XY:
                tf = False
                break
            else:
                t += A[r][i]

    if tf:
        ans = min(ans, t)

if ans == 10**8:
    print(-1)
else:
    print(ans)