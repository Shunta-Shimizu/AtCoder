from collections import defaultdict, deque
n = int(input())
graph = defaultdict(set)
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)

if len(graph[1]) == 1:
    ans = 1
else:
    A = []
    ans2 = 0
    for i in graph[1]:
        que = deque()
        que.append(i)
        nodes = {1}
        nodes.add(i)
        count = 1
        while que:
            x = que.popleft()
            count += len(graph[x])-1
            for y in graph[x]:
                if y not in nodes:
                    nodes.add(y)
                    que.append(y)
        # print(nodes)
        A.append(len(nodes))
        ans2 = max(ans2, len(nodes))
    A.sort()
    ans = 0
    for i, c in enumerate(A):
        if i >= len(graph[1])-1:
            break
        else:
            if ans == 0:
                ans += c
            else:
                ans += c-1
print(ans)
print(n-ans2)