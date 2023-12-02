n, k = map(int, input().split())
H = list(map(int, input().split()))

H.sort(reverse=True)
ans = 0
for i in range(n):
    if i+1 <= k:
        continue
    else:
        ans += H[i]

print(ans)