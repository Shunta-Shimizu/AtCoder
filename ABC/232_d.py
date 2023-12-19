from collections import defaultdict, deque
import sys
sys.setrecursionlimit(10**9)

h, w = map(int, input().split())
C = []
for _ in range(h):
    c = input()
    C.append(c)

graph = defaultdict(set)
for i in range(h):
    for j in range(w):
        if C[i][j] == ".":
            if i+1 < h:
                if C[i+1][j] == ".":
                    graph[(i, j)].add((i+1, j))
            
            if j+1 < w:
                if C[i][j+1] == ".":
                    graph[(i, j)].add((i, j+1))

que = deque()
que.append((0, 0))
nodes = {(0, 0)}
tf = [[False for _ in range(w)] for _ in range(h)]
while que:
    x = que.popleft()
    tf[x[0]][x[1]] = True
    for y in graph[x]:
        if y not in nodes:
            nodes.add(y)
            que.append(y)

ans = 0
for i in range(h):
    for j in range(w):
        if tf[i][j]:
            ans = max(ans, i+j+1)

print(ans)