n, p, q = map(int, input().split())
D = list(map(int, input().split()))

ans = q + min(D)
print(min(p, ans))