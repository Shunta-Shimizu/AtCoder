from bisect import bisect_left
n, m = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
ans = 0
for i, a in enumerate(A):
    p = bisect_left(A, a+m)
    ans = max(ans, p-i)

print(ans)