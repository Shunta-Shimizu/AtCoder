from collections import defaultdict
n, m = map(int, input().split())

graph = defaultdict(set)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

for v in graph[1]:
    if n in graph[v]:
        print("POSSIBLE")
        exit()

print("IMPOSSIBLE")
