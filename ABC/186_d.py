n = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)
dp =[[a for a in A], [0 for _ in range(n)], [0 for _ in range(n)]]
sum_A = sum(A)
for i, a in enumerate(A):
    if i == 0:
        dp[1][i] = n-i-1
        dp[2][i] = sum_A-a
    else:
        dp[1][i] = n-i-1
        dp[2][i] = sum_A-a
    sum_A -= a
# print(dp)
ans = 0
for i in range(n):
    if i == n-1:
        break
    ans += abs(dp[0][i]*dp[1][i]-dp[2][i])

print(ans)