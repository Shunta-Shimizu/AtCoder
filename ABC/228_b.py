n, x = map(int, input().split())
A = list(map(int, input().split()))

tf = [False for _ in range(n)]

ans = 0
for _ in range(n):
    if not tf[x-1]:
        tf[x-1] = True
        ans += 1
        x = A[x-1]
    else:
        break

print(ans)