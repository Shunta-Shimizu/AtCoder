n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

Xa = [0 for _ in range(n)]
Xb = [0 for _ in range(n)]
tfa = [False for _ in range(n)]
tfb = [False for _ in range(n)]
for i in range(m):
    if not tfa[A[i]-1] and not tfb[B[i]-1]:
        Xa[A[i]-1] = 0
        Xb[B[i]-1] = 1
        tfa[A[i]-1] = True
        tfb[B[i]-1] = True
        if not tfa[B[i]-1]:
            Xa[B[i]-1] = 1
            tfa[B[i]-1] = True
        if not tfb[A[i]-1]:
            Xb[A[i]-1] = 0
            tfb[A[i]-1] = True
    elif tfa[A[i]-1] and not tfb[B[i]-1]:
        Xb[B[i]-1] = 1
        tfb[B[i]-1] = True
        if not tfa[B[i]-1]:
            Xa[B[i]-1] = 0
            tfa[B[i]-1] = True
    elif not tfa[A[i]-1] and tfb[B[i]-1]:
        Xa[A[i]-1] = 1
        tfa[A[i]-1] = True
        if not tfb[A[i]-1]:
            Xb[A[i]-1] = 0
            tfb[A[i]-1] = True

for i in range(n):
    if Xa[i] != Xb[i]:
        print("No")
        exit()
    
print("Yes")