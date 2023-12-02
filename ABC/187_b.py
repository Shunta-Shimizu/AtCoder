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
        a = (Y[j] - Y[i]) / (X[j] - X[i])
        if -1 <= a <= 1:
            ans += 1

print(ans)