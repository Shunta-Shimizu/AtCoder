n = int(input())
A = []
B = []
for _ in range(n):
    a = list(map(int, input().split()))
    A.append(a)
for _ in range(n):
    b = list(map(int, input().split()))
    B.append(b)

for _ in range(5):
    tf = True
    for i in range(n):
        for j in range(n):
            if A[i][j] == 1 and B[i][j] == 0:
                    tf = False
    if tf:
        print("Yes")
        exit()
    else:    
        A_new =[[0 for _ in range(n)] for _ in range(n)]
        for l in range(n):
            for m in range(n):
                A_new[l][m] = A[n-1-m][l]
        # print(A_new)
        A = A_new

print("No")
