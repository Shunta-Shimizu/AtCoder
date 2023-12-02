from collections import defaultdict

n, m = map(int, input().split())

city = defaultdict(set)
for _ in range(m):
    a, b = map(int, input().split())
    city[a].add(b)
    city[b].add(a)

for i in range(1, n+1):
    print(len(city[i]), *sorted(city[i]), sep=" ")
