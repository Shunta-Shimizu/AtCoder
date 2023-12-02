n, k = map(int, input().split())
P = list(map(int, input().split()))

P.sort()
ans = 0
for i in range(k):
    ans += P[i]

print(ans)