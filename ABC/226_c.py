from collections import defaultdict, deque

n = int(input())
T = []
K = []
A = []
graph = defaultdict(list)
for i in range(n):
    t, k, *a = map(int, input().split())
    T.append(t)
    K.append(k)
    A.append(a)
    graph[i] = a

# que = deque()
# que.append(n)
# nodes = {n}
# ans = T[n-1]
# while que:
#     x = que.popleft()
#     for node in graph[x-1]:
#         if node not in nodes:
#             que.append(node)
#             nodes.add(node)
#             ans += T[node-1]

import sys
sys.setrecursionlimit(10**9)

ans = 0
nodes = set()
def dfs(now):
    global ans
    global nodes
    if now not in nodes:
        nodes.add(now)
        ans += T[now-1]
        for p in graph[now-1]:
            dfs(p)

dfs(n)
print(ans)