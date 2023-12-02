from collections import defaultdict, deque

n, m = map(int, input().split())
A = list(map(int, input().split()))

if m == 0:
    for i in range(n):
        print(i+1, end=" ")
    exit()
    
graph = defaultdict(list)
tf = defaultdict()
j = 0
for i in range(1, n+1):
    if j >= m - 1:
        j = m -1
    if i == A[j]:
        graph[i].append(i+1)
        graph[i+1].append(i)
        tf[i] = False
        tf[i+1] = False
        j += 1
    else:
        graph[i] = []
        tf[i] = False

graph = sorted(graph.items())
graph = dict((x, y) for x, y in graph)

pair = []
que = deque()
k = -1
for node in graph.keys():
    if not tf[node]:
        que.append(node)
        nodes = {node}
        pair.append([])
        k += 1
        while que:
            v = que.popleft()
            tf[v] = True
            pair[k].append(v)
            for x in graph[v]:
                if x not in nodes:
                    que.append(x)
                    nodes.add(x)
# print(pair)
for i in range(len(pair)):
    p = sorted(pair[i], reverse=True)
    print(*p, end=" ")

