from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
graph = defaultdict(list)
length = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    length[a-1][b-1] = c
    length[b-1][a-1] = c

ans = 0
tf = [False for _ in range(n)]

def dfs(now, d):
    global ans
    tf[now] = True
    if d > ans:
        ans = d
    for i in range(n):
        if not tf[i] and length[now][i] > 0:
            dfs(i, d+length[now][i])

    tf[now] = False

for i in range(n):
    dfs(i, 0)

print(ans)