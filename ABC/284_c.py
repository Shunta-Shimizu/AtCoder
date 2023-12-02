from collections import defaultdict, deque

n, m = map(int, input().split())

graph = defaultdict(list)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visit_node = [False] * n
graph_num = 0

for i in range(n):
    if visit_node[i] == False:
        graph_num += 1
        que = deque()
        que.append(i+1)
        nodes = {i+1}
        while que:
            x = que.popleft()
            for y in graph[x]:
                if y not in nodes:
                    que.append(y)
                    nodes.add(y)
                    visit_node[y-1] = True
        # print(nodes)

print(graph_num)