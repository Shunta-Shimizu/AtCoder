from collections import defaultdict, deque
n, m = map(int, input().split())
graph = defaultdict(set)
check = defaultdict(int)
for _ in range(m):
    u, v = map(int, input().split())
    if u == v:
        graph[u].add(v)
        check[(u, v)] += 1
    else:
        graph[u].add(v)
        graph[v].add(u)
        check[(u, v)] += 1
        check[(v, u)] += 1


tf = True
tf_nodes = [False for _ in range(n)]
for i in range(1, n+1):
    if tf_nodes[i-1]:
        continue
    else:
        que = deque()
        que.append(i)
        nodes = {i}
        edge = 0
        while que:
            x = que.popleft()
            tf_nodes[x-1] = True
            for y in graph[x]:
                if y not in nodes:
                    print([x, y])
                    edge += check[(x, y)]
                    nodes.add(y)
                    que.append(y)
                else:
                    if x == y:
                        edge += check[(x, y)]

        print("check:", len(nodes), edge)
        if len(nodes) != edge:
            tf = False

if tf:
    print("Yes")
else:
    print("No")