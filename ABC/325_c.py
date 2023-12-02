from collections import defaultdict, deque
h, w = map(int, input().split())
S = []
for _ in range(h):
    s = input()
    S.append(s)

def check_tf(i, j):
    Diff =[(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    check = True
    for d in Diff:
        if i+d[0] < 0 or i+d[0] >= h:
            continue
        else:
            if j+d[1] < 0 or j+d[1] >= w:
                continue
            else:
                if tf[i+d[0]][j+d[1]]:
                    check = False
                else:
                    if S[i+d[0]][j+d[1]] == "#":
                        tf[i+d[0]][j+d[1]] = True

    return check


tf = [[False for _ in range(w)] for _ in range(h)]
ans = 0
for i in range(h):
    for j in range(w):
        if S[i][j] == "#" and not tf[i][j]:
            que = deque()
            que.append((i, j))
            nodes = {(i, j)}
            while que:
                x = que.popleft()
                if tf[x[0]][x[1]]:
                    continue
                else:
                    tf[x[0]][x[1]] = True
                Diff = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
                for d in Diff:
                    if x[0]+d[0] < 0 or x[0]+d[0] >= h:
                        continue
                    else:
                        if x[1]+d[1] < 0 or x[1]+d[1] >= w:
                            continue
                        else:
                            if S[x[0]+d[0]][x[1]+d[1]] == "#" and not tf[x[0]+d[0]][x[1]+d[1]]:
                                que.append((x[0]+d[0], x[1]+d[1]))

            ans += 1              

print(ans)