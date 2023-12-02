n = int(input())

A = []
B = []
for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

ans = 0
for i in range(n):
    ans += A[i] * (B[i] - A[i] + 1) + ((B[i] - A[i]) / 2 * (B[i] - A[i] + 1))

print(int(ans))