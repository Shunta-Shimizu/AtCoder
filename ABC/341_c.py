h, w, n = map(int, input().split())
T = input()
d = {"L":(0, -1), "R":(0, 1), "U":(-1, 0), "D":(1, 0)}
S = []
for _ in range(h):
    s = input()
    S.append(s)

count = 0
for i in range(1, h-1):
    for j in range(1, w-1):
        if S[i][j] == "#":
            continue
        a, b = i, j
        tf = True
        for t in T:
            if t == "L":
                da = 0
                db = -1
            elif t == "R":
                da = 0
                db = 1
            elif t == "U":
                da = -1
                db = 0
            else:
                da = 1
                db = 0
            a += da
            b += db
            if S[a][b] == "#":
                tf = False
                break
        if tf:
            count += 1

print(count)