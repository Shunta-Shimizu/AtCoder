n = int(input())
W = []
X = []
for _  in range(n):
    w, x = map(int, input().split())
    W.append(w)
    X.append(x)

ans = 0
for t in range(24):
    count = 0
    for j, x in enumerate(X):
        if 9 <= (t+x)%24 <= 17:
            count += W[j]
    
    ans = max(ans, count)

print(ans)