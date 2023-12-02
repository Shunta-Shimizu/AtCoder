n, m, x = map(int, input().split())
C = []
A = []
for _ in range(n):
    c, *a = map(int, input().split())
    C.append(c)
    A.append(a)

buy = []
ans = 10**8
for i in range(1 << n):
    v = [0 for _ in range(m)]
    buy.append([])
    for j in range(n):
        if 1 & (i >> j) == 1:
            buy[-1].append(j)
    
    v = [0 for _ in range(m)]
    for k in range(m):
        for b in buy[-1]:
            v[k] += A[b][k]
    
    tf = True
    for l in v:
        if l < x:
            tf = False
    # print(v)
    if tf:
        count = 0
        for b in buy[-1]:
            count += C[b]
        
        ans = min(ans, count)

if ans == 10**8:
    print(-1)
else:
    print(ans)