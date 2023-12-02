h, w = map(int, input().split())

S = []
o_xy = []
for i in range(h):
    s = input()
    for j in range(w):
        if s[j] == "o":
            o_xy.append([i, j])
    S.append(s)

print(abs(o_xy[0][0]-o_xy[1][0]) + abs(o_xy[0][1]-o_xy[1][1]))

