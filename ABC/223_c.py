n = int(input())

A = []
B = []
for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

li = 0
ri = n-1
lx = 0
rx = 0
ans = 0
while li < ri:
    lt =(A[li]-lx) / B[li]
    rt = (A[ri]-rx) / B[ri]
    if lt < rt:
        ans += B[li]*lt
        lx = 0
        rx += B[ri]*lt
        li += 1
    else:
        ans += B[li]*rt
        rx = 0
        lx += B[li]*rt
        ri -= 1

ans += (A[li]-lx-rx) / 2
print(ans)