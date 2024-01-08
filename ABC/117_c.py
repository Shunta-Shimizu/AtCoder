n, m = map(int, input().split())
X = list(map(int, input().split()))

X.sort()
diff = []
for i in range(m-1):
    diff.append(X[i+1]-X[i])

diff.sort(reverse=True)
ans = sum(diff[n-1:])

print(ans)