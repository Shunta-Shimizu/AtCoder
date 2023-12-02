import itertools

S = []
for _ in range(9):
    s = list(map(str, input()))
    S.append(s)

ans = 0 
for x1, y1, x2, y2 in itertools.product(range(9), repeat=4):
    if x2 > x1 and y2 >= y1 and S[x1][y1] == "#" and S[x2][y2] == "#":
        dx = x2 -x1
        dy = y2 - y1
        x3 = x2 - dy
        y3 = y2 + dx
        x4 = x1 - dy
        y4 = y1 + dx

        if 0<=x3<9 and 0<=y3<9 and 0<=x4<9 and 0<=y4<9 and S[x3][y3] == "#" and S[x4][y4] == "#":
            ans += 1

print(ans)
