n = int(input())

X = []
Y = []
for _ in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            S = 0.5 * abs((X[i] - X[k]) * (Y[j] - Y[k]) - (Y[i] - Y[k]) * (X[j] - X[k]))
            if S > 0:
                # print(i, j, k)
                ans += 1

print(ans)

