n = int(input())
A = list(map(int, input().split()))

A.sort()
nf = A[0]
tf = True
for i in range(1, n):
    if A[i]-nf == 1:
        nf = A[i]
        continue
    else:
        print(nf+1)
        exit()

print(A[0])
