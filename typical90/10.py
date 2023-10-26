from collections import defaultdict
n = int(input())

ci = defaultdict(int)
dp = [[0 for _ in range(n)] for _ in range(2)]
sum1 = 0
sum2 = 0
for i in range(n):
    c, p = map(int, input().split())
    ci[i] = c
    if c == 1:
        sum1 += p
        dp[c-1][i] = sum1
        dp[1][i] = sum2
    else:
        sum2 += p
        dp[c-1][i] = sum2
        dp[0][i] = sum1

q = int(input())
ans = [] 
for i in range(q):
    l, r = map(int, input().split())
    if l >= 2:
        if l == r:
            if ci[l-1] == 1:
                ans1 = dp[0][r-1]-dp[0][l-2]
                ans2 = 0
            else:
                ans1 = 0
                ans2 = dp[1][r-1]-dp[1][l-2]
        else:
            ans1 = dp[0][r-1]-dp[0][l-2]
            ans2 = dp[1][r-1]-dp[1][l-2]
    else:
        if l == r:
            if ci[l-1] == 1:
                ans1 = dp[0][r-1]
                ans2 = 0
            else:
                ans1 = 0
                ans2 = dp[1][r-1]
        else:
            ans1 = dp[0][r-1]
            ans2 = dp[1][r-1]
    
    ans.append((ans1, ans2))

for a1, a2 in ans:
    print(a1, a2)