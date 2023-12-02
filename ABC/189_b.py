n, x = map(int, input().split())
V = []
P = []
for _ in range(n):
    v, p = map(int, input().split())
    V.append(v)
    P.append(p)

ans = -0.0000001
for i in range(n):
    ans += V[i] * P[i] / 100
    if ans > x:
        print(i+1)
        exit()

print(-1)