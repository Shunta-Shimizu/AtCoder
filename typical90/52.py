n = int(input())
A = []
for _ in range(n):
    a = list(map(int, input().split()))
    A.append(a)

ans = sum(A[0])
for i in range(1, n):
    ans *= sum(A[i])
    ans %= (10**9+7)

print(ans)