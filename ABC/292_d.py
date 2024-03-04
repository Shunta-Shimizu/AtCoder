from collections import defaultdict, deque
n, m = map(int, input().split())

graph = defaultdict(set)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)
