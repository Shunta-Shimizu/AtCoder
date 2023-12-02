from collections import defaultdict, deque
import sys
sys.setrecursionlimit(10**8)

n, x, y = map(int, input().split())

graph = defaultdict(list)
# tf = defaultdict()
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    # tf[u] = False
    # tf[v] = False

que = deque()
# que.append(x)
def DFS(now, pre):
    que.append(now)
    # print(*que)
    if now == y:
        print(*que)
        exit()
    # tf[now] = True
    for to in graph[now]:
        if to != pre:
            DFS(to, now)
    que.pop()

DFS(x, -1)
