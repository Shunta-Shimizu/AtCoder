n, m = map(int, input().split())
A = list(map(int, input().split()))

s1 = 0
t1 = 0
for i in range(m):
    s1 += (i+1) * A[i]
    t1 += 1 * A[i]

ans = s1
for i in range(n-m):
    s2 = s1 - t1 + m * A[i+m]
    t2 = t1 - A[i] + A[i+m]
    # print(s2, ans)
    ans = max(ans, s2)
    s1 = s2
    t1 = t2

print(ans)

