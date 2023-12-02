n, m = map(int, input().split())

L = []
R = []
for _ in range(m):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

l_max = max(L)
r_min = min(R)
ans = 0
for i in range(n):
    if l_max <= i+1 <= r_min:
        ans += 1

print(ans)

