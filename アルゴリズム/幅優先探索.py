# https://atcoder.jp/contests/abc007/tasks/abc007_3

from collections import deque

r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

map = [list(input()) for _ in range(r)]

dist = [[10**4 for _ in range(c)] for _ in range(r)] # 各マスの最小手数 # 10**4で仮の値を埋める

for j in range(r):
    for i in range(c):
        if map[j][i] == '#':
            dist[j][i] = -1 # 壁は-1
# print(dist)
dist[sy-1][sx-1] = 0
que = deque()
que.append([sy-1, sx-1])
# 移動の種類
move = [[1, 0], [-1, 0], [0, 1], [0, -1]]

while que:
    y, x = que.popleft()
    # print(map[y][x])
    for i, j in move:
        if y+i >= r or y+i < 0 or x+j >= c or x+j < 0:
            # print(map[y+i][x+j])
            continue
        if map[y+i][x+j] == "#":
            # print(map[y+i][x+j])
            continue
        if dist[y+i][x+j] != 10**4:
            continue

        dist[y+i][x+j] = dist[y][x] + 1
        que.append([y+i, x+j])

# print(dist)
print(dist[gy-1][gx-1])

