# 連結成分の個数を数える
# 連結成分の個数 = BFS, DFSを行った回数
from collections import defaultdict, deque

n, m = map(int, input().split())

graph = defaultdict(list)
tf = defaultdict()

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    tf[a] = False
    tf[b] = False

node_num = len(graph.keys())

# 頂点数1の孤立ノードを追加
if node_num < n:
    for i in range(1, n+1):
        if i not in graph.keys():
            graph[i] = []
            tf[i] = False

count = 0
que = deque()
for node in graph.keys():
    if not tf[node]:
        que.append(node)
        nodes = {node}

        while que:
            v = que.popleft()
            tf[v] = True
            for x in graph[v]:
                if x not in nodes:
                    que.append(x)
                    nodes.add(x)

        count += 1

print(m - n + count)