h, w, n = map(int, input().split())

grid = [["." for _ in range(w)] for _ in range(h)]

db = [(0, -1), (1, 0), (0, 1), (-1, 0)]
dw = [(0, 1), (1, 0), (0, -1), (-1, 0)]
now = 0
x = 0
y = 0
tf = False
for i in range(n):
    if i == 0:
        grid[0][0] = "#"
        x += dw[now%4][0]
        y += dw[now%4][1]
        now += 1
    else:
        if grid[x][y] == ".":
            if tf:
                now = 4-(now%4)
            grid[x][y] = "#"
            x += dw[now%4][0]
            y += dw[now%4][1]
            now += 1
            tf = False
        else:
            if not tf:
                now = 4-(now%4)
            grid[x][y] = "."
            x += db[now%4][0]
            y += db[now%4][1]
            now += 1
            tf = True
    if x < 0:
        x = h-1
    elif x >= h:
        x = 0
    if y < 0:
        y = w-1
    elif y >= w:
        y = 0

for g in grid:
    print(*g, sep="")