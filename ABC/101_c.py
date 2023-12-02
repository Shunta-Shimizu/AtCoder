n, k = map(int, input().split())
A = list(map(int, input().split()))

ans = (n+k-3) // (k-1)
print(ans)