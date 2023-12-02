# 連結成分の個数を数える
# 頂点数がXの連結成分の全域木はX-1の辺を持つ
from collections import defaultdict
import sys
sys.setrecursionlimit(10**8)

n, m = map(int, input().split())
graph = defaultdict(list)
tf = defaultdict()
nodes = set()

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    tf[a] = False
    tf[b] = False
    nodes.add(a)
    nodes.add(b)

# 頂点数1の孤立ノードを追加
if len(nodes) < n:
    for i in range(1, n+1):
        if i not in nodes:
            graph[i] = []
            tf[i] = False
            nodes.add(i)

def DFS(now):
    tf[now] = True
    for to in graph[now]:
        if not tf[to]:
            DFS(to)

count = 0
for node in nodes:
    if not tf[node]:
        DFS(node)
        count += 1

# count2 = 0
# for key, value in tf.items():
#     if value == False:
#         DFS(key)
#         count2 += 1

print(m - n + count)
# print(m - n + count2)
