from collections import defaultdict, deque

n = int(input())

# BFS
graph = defaultdict(list)
for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

que = deque()
que.append(1)
nodes = {1}

while que:
    v = que.popleft()
    for i in graph[v]:
        if not i in nodes:
            que.append(i)
            nodes.add(i)
# print(graph)
print(max(nodes))

