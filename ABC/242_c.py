n = int(input())

mod = 998244353
dp = [[0 for _ in range(9)] for _ in range(n)]

for i in range(n):
    for j in range(9):
        if i == 0:
            dp[i][j] = 1
        else:
            if j == 0:
                dp[i][j] += (dp[i-1][j] + dp[i-1][j+1])
            elif j == 8:
                dp[i][j] +=  (dp[i-1][j-1] + dp[i-1][j])
            else:
                dp[i][j] += (dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1])
        dp[i][j] %= mod

ans = sum(dp[-1][:]) % mod
print(ans)