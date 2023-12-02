n = int(input())
P = list(map(int, input().split()))

p1 = P[0]
ans = 0
tmp = 0
for i in range(1, n):
    if p1 <= P[i] and tmp < P[i]:
        ans = P[i]-p1+1
        tmp = P[i]

print(ans)