N, Q = map(int, input().split())
L =[]
a = []

for _ in range(N):
    La = list(map(int, input().split()))
    L.append(La[0])
    a.append(La[1:])

ans = []
for _ in range(Q):
    s, t = map(int, input().split())
    ans.append(a[s-1][t-1])

print(*ans, sep="\n")

