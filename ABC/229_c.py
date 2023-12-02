n, w = map(int, input().split())

weight = []
for _ in range(n):
    a, b = map(int, input().split())
    weight.append([a, b])

weight = sorted(weight, reverse=True)

ans = 0
for i in range(n):
    m = min(weight[i][1], w)
    w -= m
    if w < 0:
        w = 0
    ans += weight[i][0] * m

print(ans)