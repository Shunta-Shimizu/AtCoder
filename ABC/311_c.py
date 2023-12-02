from collections import defaultdict, deque
n = int(input())
A = list(map(int, input().split()))

graph = defaultdict(list)
for i in range(n):
    graph[i+1].append(A[i])

for i in range(n):
    ans = []
    que = deque()
    que.append(i+1)
    nodes = {i+1}
    while que:
        x = que.popleft()
        for y in graph[x]:
            if y not in nodes:
                que.append(y)
                nodes.add(y)
            else:
                que2 = deque()
                que2.append(y)
                nodes2 = {y}
                ans.append(y)
                while que2:
                    x2 = que2.popleft()
                    for y2 in graph[x2]:
                        if y2 not in nodes2:
                            que2.append(y2)
                            nodes2.add(y2)
                            ans.append(y2)
                        else:
                            print(len(ans))
                            print(*ans)
                            exit()
