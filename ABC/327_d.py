from collections import defaultdict, deque
n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

graph = defaultdict(set)
visited = defaultdict(int)
for i in range(m):
    graph[A[i]].add(B[i])
    graph[B[i]].add(A[i])
    visited[A[i]] = -1
    visited[B[i]] = -1

for a in list(graph.keys()):
    if visited[a] != -1:
        continue
    que = deque()
    que.append(a)
    visited[a] = 0
    while que:
        x = que.popleft()
        for y in graph[x]:
            if visited[y] != -1:
                if visited[y] == visited[x]:
                    print("No")
                    exit()
            else:
                if visited[x] == 0:
                    visited[y] = 1
                elif visited[x] == 1:
                    visited[y] = 0
                que.append(y)

for v in visited:
    if v == -1:
        print("No")
        exit()

print("Yes")