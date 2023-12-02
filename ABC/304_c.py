import math
from collections import defaultdict, deque
n, d = map(int, input().split())
XY = []
tf = defaultdict(bool)
graph = defaultdict(set)
for i in range(n):
    x, y = map(int, input().split())
    XY.append((x, y))
    tf[i] = False

tf[0] = True
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        else:
            dst = (XY[i][0]-XY[j][0])**2 + (XY[i][1]-XY[j][1])**2
            if dst <= d**2:
                graph[i].add(j)
                if tf[i]:
                    tf[j] = True

# print(graph)
que = deque()
que.append(0)
nodes = {0}
while que:
    v = que.popleft()
    tf[v] = True
    for x in graph[v]:
        if x not in nodes:
            que.append(x)
            nodes.add(x)

for t in tf.values():
    if t:
        print("Yes")
    else:
        print("No")
