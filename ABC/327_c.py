A = []
for _ in range(9):
    a = list(map(int, input().split()))
    A.append(a)

for i in range(9):
    ai = set()
    for j in range(9):
        ai.add(A[i][j])
    
    if len(ai) < 9:
        print("No")
        exit()

for j in range(9):
    aj = set()
    for i in range(9):
        aj.add(A[i][j])
    
    if len(aj) < 9:
        print("No")
        exit()

for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        akl = set()
        for k in range(i, i+3):
            for l in range(j, j+3):
                akl.add(A[k][l])
            
        if len(akl) < 9:
            # print(akl)
            # print(k, l)
            print("No")
            exit()
print("Yes")
