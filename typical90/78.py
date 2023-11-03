from collections import defaultdict
n, m = map(int, input().split())

graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    if a > b:
        graph[a].append(b)
    elif b > a:
        graph[b].append(a)

ans = 0
for k, v in graph.items():
    if len(v) == 1:
        ans += 1

print(ans)