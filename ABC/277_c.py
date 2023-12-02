from collections import defaultdict, deque

N = int(input())

G = defaultdict(list)
que = deque()
que.append(1)
for _ in range(N):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

S = {1}
while que:
    v = que.popleft()
    for i in G[v]:
        if not i in S:
            que.append(i)
            S.add(i)

print(max(S))
