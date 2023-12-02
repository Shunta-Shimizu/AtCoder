n, m , t = map(int, input().split())

A = []
B = []
for _ in range(m):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

res_n = n
t_s = 0
for i in range(m):
    res_n -= A[i] - t_s
    if res_n <= 0:
        print("No")
        exit()
    if res_n != n:
        res_n += B[i] - A[i]
        if res_n > n:
            res_n = n

    t_s = B[i]

res_n -= t - t_s

if res_n <= 0:
    print("No")
    exit()

print("Yes")