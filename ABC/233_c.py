import sys
sys.setrecursionlimit(10**9)

n, x = map(int, input().split())
L = []
A = []
for _ in range(n):
    La = list(map(int, input().split()) )
    L.append(La[0])
    A.append(La[1:])

ans = 0
def dfs(i, p):
    global ans
    if i == n:
        if p == x:
            ans += 1
    else:
        for j in range(len(A[i])):
            if p*A[i][j] > x:
                continue
            else:
                dfs(i+1, p*A[i][j])

dfs(0, 1)
print(ans)
