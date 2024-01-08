n, x = map(int, input().split())

dp = [False for _ in range(10**4+1)]
dp[0] = True
for _ in range(n):
    a, b = map(int, input().split())
    tf = []
    for i in range(len(dp)):
        for j in range(1, b+1):
            if dp[i]:
                if i+a*j < len(dp):
                    tf.append(i+a*j)

    for i in tf:
        dp[i] = True

if dp[x]:
    print("Yes")
else:
    print("No")