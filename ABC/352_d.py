n, l = map(int, input().split())

A = []
for i in range(1, n+1):
    A.append(l+i-1)

A_sum = sum(A)
tmp = 10**9
idx = 10**9
for i, a in enumerate(A):
    if abs(a) <= tmp:
        tmp = abs(a)
        idx = i+1

ans = 0
for a in A:
    if a != l+idx-1:
        ans += a

print(ans)