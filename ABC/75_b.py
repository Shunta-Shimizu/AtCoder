h, w = map(int, input().split())
S = []
for _ in range(h):
    s = list(input())
    S.append(s)

grid = [[0 for _ in range(w)] for _ in range(h)]
dx = [-1, 0, 1]
dy = [-1, 0, 1]
for i in range(h):
    for j in range(w):
        if S[i][j] == "#":
            grid[i][j] = "#"
        else:
            for x in dx:
                for y in dy:
                    if x == 0 and y == 0:
                        continue
                    else:
                        if 0 <= i+x < h and 0<= j+y < w:
                            if S[i+x][j+y] == "#":
                                grid[i][j] += 1

for g in grid:
    print(*g, sep="")