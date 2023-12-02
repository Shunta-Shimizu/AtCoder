from collections import defaultdict, deque

n, x, y = map(int, input().split())

graph = defaultdict(list)

for _ in range(1, n):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
# print(graph)

que = deque()
que.append(x)
nodes = [x]

while que:
    node = que.popleft()
    if y in graph[node]:
        nodes.append(y)
        break
    else:
        for i in graph[node]:
            if i not in nodes:
                que.append(i)
                nodes.append(i)

print(*nodes)