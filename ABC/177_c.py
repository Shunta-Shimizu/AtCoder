n = int(input())
A = list(map(int, input().split()))

ans = 0
A_sum = A[0]
for i in range(1, n):
    ans += A_sum * A[i]
    A_sum += A[i]

    ans %= 10**9+7

print(ans)
