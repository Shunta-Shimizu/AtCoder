X, K = map(int, input().split())

for i in range(1, K+1):
    y = X % 10**i // 10**(i-1)
    if y < 5:
        X_str = str(X // 10**i) + "0"*i
    else:
        X_str = str(X // 10**i + 1) + "0"*i
    X = int(X_str)
print(X)