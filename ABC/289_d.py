n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
x = int(input())

dp = [False for _ in range(x+1)]
mochi = [False for _ in range(x+1)]

for i in range(m):
    mochi[B[i]] = True

dp[0] = True
for i in range(x+1):
    if i == 0:
        for j in range(n):
            if A[j] < x+1:
                if not mochi[A[j]]:
                    dp[A[j]] = True
    else:
        if dp[i]:
            for j in range(n):
                if i+A[j] < x+1:
                    if not mochi[i+A[j]]:
                        dp[i+A[j]] = True

# print(dp)
# print(mochi)
if dp[-1]:
    print("Yes")
else:
    print("No")