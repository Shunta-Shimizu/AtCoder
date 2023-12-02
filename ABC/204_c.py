from collections import defaultdict, deque
n, m = map(int, input().split())

graph = defaultdict(set)
for i in range(n):
    graph[i+1].add(i+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)

ans = 0
for i in list(graph.keys()):
    que = deque()
    que.append(i)
    nodes = {i}
    while que:
        x = que.popleft()
        ans += 1
        for y in graph[x]:
            if y not in nodes:
                nodes.add(y)
                que.append(y)

print(ans)