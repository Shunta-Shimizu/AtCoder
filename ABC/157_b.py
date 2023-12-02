A = []
for _ in range(3):
    A.append(list(map(int, input().split())))

n = int(input())
TF = [[False, False, False] for _  in range(3)]
for i in range(n):
    b = int(input())
    for j in range(3):
        for k in range(3):
            if A[j][k] == b:
                TF[j][k] = True

bingo = False
if TF[0][0] and TF[0][1] and TF[0][2]:
    bingo = True
if TF[0][0] and TF[1][0] and TF[2][0]:
    bingo = True
if TF[0][0] and TF[1][1] and TF[2][2]:
    bingo = True
if TF[0][1] and TF[1][1] and TF[2][1]:
    bingo = True
if TF[0][2] and TF[1][2] and TF[2][2]:
    bingo = True
if TF[0][2] and TF[1][1] and TF[2][0]:
    bingo = True
if TF[1][0] and TF[1][1] and TF[1][2]:
    bingo = True
if TF[2][0] and TF[2][1] and TF[2][2]:
    bingo = True

if bingo:
    print("Yes")
else:
    print("No")