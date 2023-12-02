n, x = map(int, input().split())
A = []
B = []
for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

dp = [[False for _ in range(x)] for _ in range(n)]
for i in range(n):
    if i == 0:
        if A[i]-1 < x:
            dp[i][A[i]-1] = True
        if B[i]-1 < x:
            dp[i][B[i]-1] = True
    else:
        for j in range(x):
            if dp[i-1][j]:
                if j+A[i] < x:
                    dp[i][j+A[i]] = True
                if j+B[i] < x:
                    dp[i][j+B[i]] = True
# print(dp)
# print(dp[n-1][:])
if dp[n-1][x-1]:
    print("Yes")
else:
    print("No")
