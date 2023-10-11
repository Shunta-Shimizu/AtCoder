# 最大和
# n = int(input())
# A = list(map(int, input().split()))

# dp = [0] * (n+1)
# for i in range(n):
#     dp[i+1] = max(dp[i], dp[i] + A[i])

# print(dp[n]) 


# ナップサック問題
# n, w = map(int, input().split())

# W = []
# V = []
# for _ in range(n):
#     w_i, v_i = map(int, input().split())
#     W.append(w_i)
#     V.append(v_i)

# dp = [[0] * (w + 1) for _ in range(n+1)]

# for i in range(n):
#     for j in range(w+1):
#         if j >= W[i]:
#             dp[i+1][j] = max(dp[i][j-W[i]] + V[i], dp[i][j])
#         else:
#             dp[i+1][j] = dp[i][j]

# print(dp[n][w])


# 部分和
# n, m = map(int, input().split())
# A = list(map(int, input().split()))

# dp = [[False] * (m + 1) for _ in range(n+1)]
# dp[0][0] = True

# for i in range(n):
#     for j in range(m+1):
#         if dp[i][j]:
#             dp[i+1][j] = True
#         if j >= A[i]:
#             if dp[i][j-A[i]]:
#                 dp[i+1][j] = True

# if dp[n][m]:
#     print("Yes")
# else:
#     print("No")


# 部分和数え上げ問題
# n, m = map(int, input().split())
# A = list(map(int, input().split()))

# dp = [[0] * (m + 1) for _ in range(n+1)]
# dp[0][0] = 1

# for i in range(n):
#     for j in range(m+1):
#         dp[i+1][j] += dp[i][j]
#         dp[i+1][j] %= 1000
#         if j >= A[i]:
#             dp[i+1][j] += dp[i][j-A[i]]
#             dp[i+1][j] %= 1000

# print(dp)
# print(dp[n][m])


# 最小個数部分和問題
# n, m = map(int, input().split())
# A = list(map(int, input().split()))

# dp = [[10**8] * (m + 1) for _ in range(n + 1)]
# dp[0][0] = 0

# for i in range(n):
#     for j in range(m+1):
#         dp[i+1][j] = min(dp[i+1][j], dp[i][j])
#         if j >= A[i]:
#             dp[i+1][j] = min(dp[i+1][j-A[i]] + 1, dp[i][j])
# # print(dp)
# if dp[n][m] < 10 ** 8:
#     print(dp[n][m])
# else:
#     print(-1)


# K個以内の部分和問題
# n, m, k = map(int, input().split())
# A = list(map(int, input().split()))

# dp = [[10 ** 8] * (m + 1) for _ in range(n + 1)]
# dp[0][0] = 0

# for i in range(n):
#     for j in range(m + 1):
#         dp[i+1][j] = min(dp[i+1][j], dp[i][j])
#         if j >= A[i]:
#             dp[i+1][j] = min(dp[i+1][j-A[i]] + 1, dp[i][j])

# # print(dp[n][m])
# if dp[n][m] <= k:
#     print("Yes")
# else:
#     print("No")


# 個数制限付き部分和問題
n, m = map(int, input().split())

A = []
B = []
for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

dp = [[10 ** 8] * (m+1) for _ in range(n+1)]
dp[0][0] = 0 

for i in range(n):
    for j in range(m+1):
        if dp[i][j] < 10 ** 8:
            dp[i+1][j] = 0
        if j >= A[i]:
            if dp[i][j-A[i]] < 10 ** 8:
                dp[i+1][j] = min(dp[i+1][j], 1)
            if dp[i+1][j-A[i]] < B[i]:
                dp[i+1][j] = min(dp[i+1][j-A[i]] + 1, dp[i+1][j])

if dp[n][m] < 10 ** 8:
    print("Yes")
else:
    print("No")            
