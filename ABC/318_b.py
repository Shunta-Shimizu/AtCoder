n = int(input())
A = []
B = []
C = []
D = []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

ans = 0
for i in range(101):
    for j in range(101):
        tf = False
        for k in range(n):
            if (A[k] <= i <= B[k] and A[k] < i+1 <= B[k]) and (C[k] <= j <= D[k] and C[k] < j+1 <= D[k]):
                tf = True
            
        if tf:
            ans += 1

print(ans)