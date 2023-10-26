h, w = map(int, input().split())
A = []
for _ in range(h):
    a = list(map(int, input().split()))
    A.append(a)

sum_w = [0 for _ in range(w)]
sum_h = [0 for _ in range(h)]

for i in range(h):
    for j in range(w):
        sum_w[j] += A[i][j]

for i in range(w):
    for j in range(h):
        sum_h[j] += A[j][i]

B = [[0 for _ in range(w)] for _ in range(h)]
for i in range(h):
    for j in range(w):
        B[i][j] = sum_h[i]+sum_w[j]-A[i][j]

for b in B:
    print(*b)