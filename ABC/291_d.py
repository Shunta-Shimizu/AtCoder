n = int(input())

A = []
B = []
for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

dp = [[0] * 2 for _ in range(n+1)]
dp[0][0] = 1
dp[0][1] = 1

for i in range(1, n):
    if A[i] != A[i-1]:
        dp[i][0] += dp[i-1][0]
    if A[i] != B[i-1]:
        dp[i][0] += dp[i-1][1]
    if B[i] != A[i-1]:
        dp[i][1] += dp[i-1][0]
    if B[i] != B[i-1]:
        dp[i][1] += dp[i-1][1]
    
    dp[i][0] %= 998244353
    dp[i][1] %= 998244353

ans = (dp[n-1][0] + dp[n-1][1]) % 998244353

print(ans)

