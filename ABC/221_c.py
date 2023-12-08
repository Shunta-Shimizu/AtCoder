S = input()

n = len(S)
dp = [[0 for _ in range(n)] for _ in range(8)]
R = "chokudai"
for i in range(n):
    for j in range(8):
        if j == 0:
            if S[i] == R[j]:
                if i == 0:
                    dp[j][i] = 1
                else:
                    dp[j][i] = dp[j][i-1]+1
            else:
                dp[j][i] = dp[j][i-1]
        else:
            if S[i] != R[j]:
                dp[j][i] = dp[j][i-1]
            else:
                dp[j][i] = (dp[j][i-1] + dp[j-1][i-1]) % (10**9+7)
# print(dp)
print(dp[-1][-1])
