from collections import defaultdict, deque
n = int(input())
C = []
P = defaultdict(list)
for i in range(n):
    cp = list(map(int, input().split()))
    C.append(cp[0])
    P[i+1] = cp[1:]

ans = 10**8
for p in P[1]:
    que = deque()
    que.append(p)
    nodes = {p}
    ans_l = []
    while que:
        x = que.popleft()
        for y in P[x]:
            if y not in nodes:
                nodes.add(y)
                que.append(y)