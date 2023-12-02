n, m = map(int, input().split())
S = []
for _ in range(n):
    s = input()
    S.append(s)

for i in range(n-8):
    for j in range(m-8):
        if S[i][j] == "#":
            tf =  True
            for k in range(i, i+3):
                for l in range(j, j+3):
                    if S[k][l] != "#":
                        tf = False
            for a in range(i, i+4):
                if S[a][j+3] != ".":
                    tf = False
            for b in range(j, j+4):
                if S[i+3][b] != ".":
                    tf = False
            for x in range(i+6, i+9):
                for y in range(j+6, j+9):
                    if S[x][y] != "#":
                        tf = False
            for c in range(i+5, i+9):
                if S[c][j+5] != ".":
                    tf = False
            for d in range(j+5, j+9):
                if S[i+5][d] != ".":
                    tf = False
        else:
            tf = False
        if tf:
            print(i+1, j+1)
