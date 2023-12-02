from collections import defaultdict
n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[False for _ in range(n)] for _ in range(2)]
dp[0][0] = True
dp[1][0] = True
for i in range(1, n):
    if dp[0][i-1]:
        if abs(A[i-1]-A[i]) <= k:
            dp[0][i] = True
        if abs(A[i-1]-B[i]) <= k:
            dp[1][i] = True
    if dp[1][i-1]:
        if abs(B[i-1]-A[i]) <= k:
            dp[0][i] = True
        if abs(B[i-1]-B[i]) <= k:
            dp[1][i] = True

    if not dp[0][i] and not dp[1][i]:
        print("No")
        exit()
    # print(dp)
print("Yes")
