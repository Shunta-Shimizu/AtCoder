n = int(input())
X = list(map(int, input().split()))

x_min = min(X)
x_max = max(X)
ans = 10 ** 8
for i in range(x_min, x_max+1):
    dist = 0
    for x in X:
        dist += (x-i)**2
    ans = min(ans, dist)

print(ans)