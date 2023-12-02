h, w = map(int, input().split())

A = []
a_min = 101
for _ in range(h):
    A_i = list(map(int, input().split()))
    if min(A_i) < a_min:
        a_min = min(A_i)
    A.append(A_i)

ans = 0
for i in range(h):
    for j in range(w):
        ans += A[i][j] - a_min

print(ans)