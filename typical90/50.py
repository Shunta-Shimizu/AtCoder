n, l = map(int, input().split())

dp = [0 for _ in range(n+1)]
for i in range(n+1):
    if i == 0:
        dp[i] = 1
    else:
        if i < l:
            dp[i] = 1
        else:
            dp[i] = (dp[i-1] + dp[i-l]) % (10**9+7)

print(dp[n])