n, k = map(int, input().split())

a = n // k
n = n - k*a

ans = min(n, abs(n-k))
print(ans)