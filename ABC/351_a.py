# h, w = map(int, input().split())
# S = []
# for _ in range(h):
#     s = list(input())
#     S.append(s)


from collections import deque

H, W = map(int, input().split())
S = [input() for _ in range(H)]

def bfs(x, y):
    distance = [[-1] * W for _ in range(H)]
    distance[x][y] = 0
    queue = deque([(x, y)])
    count = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and S[nx][ny] == '.' and distance[nx][ny] == -1:
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))
                count += 1
    return count

max_freedom = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '.' and bfs(i, j) > max_freedom: # 修正点: 自由度の計算方法を修正
            max_freedom = bfs(i, j)

print(max_freedom)
