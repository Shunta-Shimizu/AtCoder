h, w, k = map(int, input().split())
S = []
for _ in range(h):
    s = list(input())
    S.append(s)

ans = set()
count1 = []
for i in range(h):
    c = []
    for j in range(w):
        if j == 0:
            if S[i][j] == "o":
                c.append(["o.", 1]) #, [1, 0]])
            elif S[i][j] == ".":
                c.append(["o.", 1]) #, [0, 1]])
            else:
                c.append([S[i][j], 1])
        else:
            if S[i][j] == c[-1][0]:
                c[-1][1] += 1
            elif c[-1][0] == "o." and S[i][j] == "o":
                c[-1][1] += 1
                # c[-1][2][0] += 1
            elif c[-1][0] == "o." and S[i][j] == ".":
                c[-1][1] += 1
                # c[-1][2][1] += 1
            else:
                if S[i][j] == "o":
                    c.append(["o.", 1]) #, [1, 0]])
                elif S[i][j] == ".":
                    c.append(["o.", 1]) #, [0, 1]])
                else:
                    c.append([S[i][j], 1])
    count1.append(c)

St = [list(x) for x in zip(*S)]
count2 = []
for i in range(w):
    c = []
    for j in range(h):
        if j == 0:
            if St[i][j] == "o":
                c.append(["o.", 1]) #, [1, 0]])
            elif St[i][j] == ".":
                c.append(["o.", 1]) #, [0, 1]])
            else:
                c.append([St[i][j], 1])
        else:
            if St[i][j] == c[-1][0]:
                c[-1][1] += 1
            elif c[-1][0] == "o." and St[i][j] == "o":
                c[-1][1] += 1
                # c[-1][2][0] += 1
            elif c[-1][0] == "o." and St[i][j] == ".":
                c[-1][1] += 1
                # c[-1][2][1] += 1
            else:
                if St[i][j] == "o":
                    c.append(["o.", 1]) #, [1, 0]])
                elif St[i][j] == ".":
                    c.append(["o.", 1]) #, [0, 1]])
                else:
                    c.append([St[i][j], 1])
    count2.append(c)

ans = 10**8
for ci in count1:
    a = 0
    for i, cij in enumerate(ci):
        # print(cij)
        if cij[0] == "o.":
            if cij[1] >= k:
                b = 0
                c = 0
                for j, s in enumerate(S[i]):
                    if s == "x":
                        b = 0
                        c = 0
                    else:
                        if s == ".":
                            b += 1
                            c += 1
                        else:
                            c += 1
                    if c == k:
                        ans = min(ans, b)

for ci in count2:
    a = 0
    for i, cij in enumerate(ci):
        # print(cij)
        if cij[0] == "o.":
            if cij[1] >= k:
                b = 0
                c = 0
                for j, st in enumerate(St[i]):
                    if st == "x":
                        b = 0
                        c = 0
                    else:
                        if st == ".":
                            b += 1
                            c += 1
                        else:
                            c += 1
                    if c == k:
                        ans = min(ans, b)
print(ans)