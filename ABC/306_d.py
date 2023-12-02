n = int(input())
X = []
Y = []
for _ in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

dp = [[0 for _ in range(n)] for _ in range(2)]
for i in range(n):
    if X[i] == 0:
        if i == 0:
            dp[0][i] = max(0, Y[i])
            dp[1][i] = max(0, Y[i])
        else:
            dp[0][i] = dp[0][i-1]
            if Y[i] < 0:
                dp[1][i] = max(dp[0][i-1]+Y[i], dp[1][i-1])
            else:
                dp[1][i] = max(dp[0][i-1]+Y[i], dp[1][i-1]+Y[i])
    else:
        if i == 0:
            dp[0][i] = max(0, Y[i])
            dp[1][i] = 0
        else:
            dp[0][i] = max(dp[0][i-1], dp[1][i-1]+Y[i])
            dp[1][i] = dp[1][i-1]

# print(dp)
print(max(dp[0][n-1], dp[1][n-1]))

