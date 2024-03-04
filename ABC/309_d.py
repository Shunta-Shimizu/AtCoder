from collections import defaultdict, deque
n1, n2, m = map(int, input().split())

graph = defaultdict(set)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

cnt1 = defaultdict(int)
que = deque()
que.append(1)
nodes = {1}
count = 0
while que:
    x = que.popleft()
    for y in graph[x]:
        if y not in nodes:
            cnt1[y] = cnt1[x]+1
            que.append(y)
            nodes.add(y)

cnt2 = defaultdict(int)
que = deque()
que.append(n1+n2)
nodes = {n1+n2}
count = 0
while que:
    x = que.popleft()
    for y in graph[x]:
        if y not in nodes:
            cnt2[y] = cnt2[x]+1
            que.append(y)
            nodes.add(y)

ans1 = 0
ans2 = 0
if len(list(cnt1.values())) > 0:
    ans1 = max(list(cnt1.values()))
if len(list(cnt2.values())) > 0:
    ans2 = max(list(cnt2.values()))

ans = ans1+ans2+1
print(ans)