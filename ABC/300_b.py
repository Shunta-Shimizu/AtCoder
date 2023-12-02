h, w = map(int, input().split())
A = []
for _ in range(h):
    a = list(input())
    A.append(a)

B = []
for _ in range(h):
    b = list(input())
    B.append(b)

A_org = A
tf = True
if A == B:
    print("Yes")
    exit()
else:
    for i in range(h):
        for j in range(w):
            c = (i, j)
            for _ in range(c[0]):
                A_new = [[0 for _ in range(w)] for _ in range(h)]
                for k in range(h):
                    for l in range(w):
                        if k == h-1:
                            A_new[k][l] = A[0][l]
                        else:
                            A_new[k][l] = A[k+1][l]
                A = A_new
                if A == B:
                    # print(A)
                    print("Yes")
                    exit()
            
            for _ in range(c[1]):
                A_new = [[0 for _ in range(w)] for _ in range(h)]
                for x in range(h):
                    for y in range(w):
                        if y == w-1:
                            A_new[x][y] = A[x][0]
                        else:
                            A_new[x][y] = A[x][y+1]
                A = A_new
                if A == B:
                    # print(A)
                    print("Yes")
                    exit()                    
            # print(A)
print("No")
    
            
