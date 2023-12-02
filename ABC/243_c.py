from collections import defaultdict
n = int(input())

XY = []
for _ in range(n):
    x, y = map(int, input().split())
    XY.append((x, y))

S = input()
sxy = defaultdict(str)
for i in range(n):
    sxy[XY[i]] = S[i]

sxy = dict(sorted(sxy.items(), key=lambda x:x[0][0]))
sy = defaultdict(list)
for xy, s in sxy.items():
    if len(sy[xy[1]]) == 0:
        sy[xy[1]].append(s)
    else:
        if s == "R" and sy[xy[1]][-1] == "L":
            sy[xy[1]].append(s)
        elif s == "L" and sy[xy[1]][-1] == "R":
            print("Yes")
            exit()

print("No")

