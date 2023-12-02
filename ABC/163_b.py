n, m = map(int, input().split())
A = list(map(int, input().split()))

for i in range(m):
    n -= A[i]

if n < 0:
    print(-1)
else:
    print(n)
