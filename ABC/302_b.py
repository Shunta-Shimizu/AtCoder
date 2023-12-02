h, w = map(int, input().split())

S = []
for _ in range(h):
    s = list(input())
    S.append(s)

ans = []
for i in range(h):
    for j in range(w):
        if S[i][j] == "s":
            if i+5 <= h:
                if S[i+1][j] == "n":
                    if S[i+2][j] == "u":
                        if S[i+3][j] == "k":
                            if S[i+4][j] == "e":
                                for k in range(1, 6):
                                    print(i+k, j+1)
                                exit()
            if j+5 <= w:
                if S[i][j+1] == "n":
                    if S[i][j+2] == "u":
                        if S[i][j+3] == "k":
                            if S[i][j+4] == "e":
                                for k in range(1, 6):
                                    print(i+1, j+k)
                                exit()
            if i+5 <= h and j+5 <= w:
                if S[i+1][j+1] == "n":
                    if S[i+2][j+2] == "u":
                        if S[i+3][j+3] == "k":
                            if S[i+4][j+4] == "e":
                                for k in range(1, 6):
                                    print(i+k, j+k)
                                exit()
            if i-4 >= 0 and j-4 >= 0:
                if S[i-1][j-1] == "n":
                    if S[i-2][j-2] == "u":
                        if S[i-3][j-3] == "k":
                            if S[i-4][j-4] == "e":
                                for k in range(5):
                                    print(i-k+1, j-k+1)
                                exit()

            if i+5 <= h and j-4 >= 0:
                if S[i+1][j-1] == "n":
                    if S[i+2][j-2] == "u":
                        if S[i+3][j-3] == "k":
                            if S[i+4][j-4] == "e":
                                for k in range(5):
                                    print(i+k+1, j-k+1)
                                exit()

            if i-4 >= 0 and j+5 <= w:
                if S[i-1][j+1] == "n":
                    if S[i-2][j+2] == "u":
                        if S[i-3][j+3] == "k":
                            if S[i-4][j+4] == "e":
                                for k in range(5):
                                    print(i-k+1, j+k+1)
                                exit()
            if i-4 >= 0:
                if S[i-1][j] == "n":
                    if S[i-2][j] == "u":
                        if S[i-3][j] == "k":
                            if S[i-4][j] == "e":
                                for k in range(5):
                                    print(i-k+1, j+1)
                                exit()
            if j-4 >= 0:
                if S[i][j-1] == "n":
                    if S[i][j-2] == "u":
                        if S[i][j-3] == "k":
                            if S[i][j-4] == "e":
                                for k in range(5):
                                    print(i+1, j-k+1)
                                exit()                              

