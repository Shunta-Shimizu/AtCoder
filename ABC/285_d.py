from collections import defaultdict, deque

n = int(input())
graph = defaultdict(list)
names = set()
count = defaultdict(int)

for _ in range(n):
    s, t = map(str, input().split())
    graph[s].append(t)
    graph[t].append(s)
    count[t] += 1
    count[s] += 1
    names.add(s)
    names.add(t)

names = list(names)
# print(graph)
# print(names)
num = 0
for name in names:
    if count[name] == 2:
        num += 1
    elif count[name] == 0 or count[name] > 2:
        print("No")
        exit()
# print(count)
# print(num)
if num == n:
    print("No")
    exit()

tf = [False] * len(names)
for i in range(len(names)):
    if tf[i] == False:
        que = deque()
        que.append(names[i])
        nodes = {names[i]}
        while que:
            j = que.popleft()
            for k in graph[j]:
                if k not in nodes:
                    que.append(k)
                    nodes.add(k)
                    tf[i] = True

if tf:
    print("Yes")
else:
    print("No")