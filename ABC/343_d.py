from collections import defaultdict
n, t = map(int, input().split())

point = defaultdict(int)
count = defaultdict(int)
count[0] = n
k = {0}
ans = 1
c = []
for _ in range(t):
    a, b = map(int, input().split())
    count[point[a]] -= 1
    count[point[a]+b] += 1
    point[a] += b

    if count[point[a]-b] <= 0:
        ans -= 1

    if point[a] not in k:
        ans += 1
        k.add(point[a])
    else:
        if count[point[a]] == 1:
            ans += 1

    c.append(ans)

for i in c:
    print(i)