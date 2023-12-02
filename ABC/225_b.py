from collections import defaultdict

n = int(input())

graph = defaultdict(list)
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

tf = False
for key in graph.keys():
    if len(graph[key]) == n - 1:
        tf = True

if tf:
    print("Yes")
else:
    print("No")
