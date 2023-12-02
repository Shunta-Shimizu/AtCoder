n, h, x = map(int, input().split())
P = list(map(int, input().split()))

ans = []
for i in range(n):
    if h+P[i] >= x:
        ans.append([i+1, P[i]])

ans = sorted(ans, key=lambda x:x[1])
print(ans[0][0])