from collections import defaultdict, deque

n, m = map(int, input().split())

graph = defaultdict(list)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

one_count = 0
two_count = 0
for i in range(n):
    if len(graph[i+1]) > 2:
        print("No")
        exit()
    elif len(graph[i+1]) == 1:
        fnode = i+1
        one_count += 1
    elif len(graph[i+1]) == 2:
        two_count += 1
    else:
        print("No")
        exit()

if one_count != 2:
    print("No")
    exit()
else:
    if two_count != n-2:
        print("No")
        exit()

que = deque()
que.append(fnode)
node = {fnode}

count = 0
while que:
    v = que.popleft()
    count += 1
    for j in graph[v]:
        if not j in node:
            que.append(j)
            node.add(j)

if count == n:
    print("Yes")
else:
    print("No")