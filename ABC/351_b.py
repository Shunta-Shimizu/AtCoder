n = int(input())
A = []
B = []
for _ in range(n):
    a = list(input())
    A.append(a)

for _ in range(n):
    b = list(input())
    B.append(b)

for i in range(n):
    if A[i] != B[i]:
        for j in range(n):
            if A[i][j] != B[i][j]:
                print(i+1, j+1)
                exit()
