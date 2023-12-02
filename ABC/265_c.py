h, w = map(int, input().split())

grid = []
for _ in range(h):
    G = list(input())
    grid.append(G)

now = (0, 0)
move = ((now[0]-1, now[1]), (now[0]+1, now[1]), (now[0], now[1]-1), (now[0], now[1]+1))

passed_grid = set()
while True:
    if now in passed_grid:
        print(-1)
        exit()
    g = grid[now[0]][now[1]]
    passed_grid.add(now)
    if g == "U":
        if now[0] == 0:
            break
        else:
            now = (now[0]-1, now[1])
    elif g == "D":
        if now[0] == h-1:
            break
        else:
            now = (now[0]+1, now[1])
    elif g == "L":
        if now[1] == 0:
            break
        else:
            now = (now[0], now[1]-1)
    else:
        if now[1] == w-1:
            break
        else:
            now = (now[0], now[1]+1)

print(now[0]+1, now[1]+1)