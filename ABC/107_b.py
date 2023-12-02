h, w = map(int, input().split())

A = []
for _ in range(h):
    a = list(input())
    if a.count("#") != 0:
        A.append(a)

ans = []
if len(A) == 0:
    print(*ans)
else:
    h = len(A)
    w = len(A[0])
    A_T = list(zip(*A))
    for i in range(w):
        if A_T[i].count("#") != 0:
            ans.append(A_T[i])
    
    ans = list(zip(*ans))
    for a in ans:
        print(*a, sep="")