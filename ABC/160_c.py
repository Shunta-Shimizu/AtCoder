k, n = map(int, input().split())
A = list(map(int, input().split()))

ans = A[n-1] - A[0]
for i in range(1, n):
    dist = k-A[i] + A[i-1]
    ans = min(ans, dist)

print(ans)