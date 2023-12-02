n = int(input())
P = list(map(int, input().split()))

p_min = 10 ** 8
ans = 0
for i in range(n):
    p_min = min(p_min, P[i])
    if p_min == P[i]:
        ans += 1

print(ans)