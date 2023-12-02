r, c = map(int, input().split())
B = []
for _ in range(r):
    b = list(input())
    B.append(b)

tf = [[False for _ in range(c)] for _ in range(r)] 
for i in range(r):
    for j in range(c):
        if B[i][j] != "." and B[i][j] != "#":
            num = int(B[i][j])
            tf[i][j] = "."
            for k in range(r):
                for l in range(c):
                    if B[k][l] == "." or B[k][l] == "#":
                        if abs(i-k)+abs(j-l) <= num:
                            tf[k][l] = True

for i in range(r):
    for j in range(c):
        if tf[i][j]:
            B[i][j] = "."


for i in range(r):
    print(*B[i], sep="")



