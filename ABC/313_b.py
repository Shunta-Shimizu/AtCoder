n, m = map(int, input().split())
num = {i for i in range(1, n+1)}
for _ in range(m):
    a, b = map(int, input().split())
    num.discard(b)

if len(num) == 1:
    print(*num)
else:
    print(-1)