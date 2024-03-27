n, x = map(int, input().split())
AB = []
for _ in range(n):
    a, b = map(int, input().split())
    AB.append([a, b])

dp = [0 for _ in range(n)]
count = 0
ans = 10**30
for i in range(n):
    if i == 0:
        dp[i] = sum(AB[i])
    else:
        dp[i] = dp[i-1]+sum(AB[i])
    count += 1
    ans = min(ans, dp[i]+AB[i][1]*(x-count))
    if x-count < 0:
        break

print(ans)