from collections import defaultdict, deque
n = int(input())

graph = defaultdict(set)
D = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1)]
A = set()
tf = defaultdict(bool)
for i in range(n):
    x, y = map(int, input().split())
    A.add((x, y))
    tf[(x, y)] = False
    if i == 0:
        graph[(x, y)] = set()
    else:
        for dx, dy in D:
            if (x+dx, y+dy) in A:
                graph[(x, y)].add((x+dx, y+dy))
                graph[(x+dx, y+dy)].add((x, y))

ans = 0
for k, v in tf.items():
    if v:
        continue
    else:
        ans += 1
        que = deque()
        que.append(k)
        nodes = {k} 
        while que:
            xy = que.popleft()
            tf[xy] = True
            for x, y in graph[xy]:
                if (x, y) not in nodes:
                    que.append((x, y))
                    nodes.add((x, y))

print(ans)
