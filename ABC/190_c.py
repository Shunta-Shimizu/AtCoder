n, m = map(int, input().split())
AB = []
for _ in range(m):
    a, b = map(int, input().split())
    AB.append((a, b))

k = int(input())
CD = []
for _ in range(k):
    c, d = map(int, input().split())
    CD.append((c, d))

ans = 0
for i in range(1, 1 << k):
    dishes = set()
    for j in range(k):
        if 1 & (i >> j) == 1:
            dishes.add(CD[j][1])
        else:
            dishes.add(CD[j][0])
    count = 0
    # print(dishes)
    for l in range(m):
        if AB[l][0] in dishes and AB[l][1] in dishes:
            count += 1
    ans = max(ans, count)

print(ans)

