import math

n = int(input())

XY = []
for _ in range(n):
    xy = list(map(int, input().split()))
    XY.append(xy)

max_num = 0
for i in range(n):
    for j in range(i, n):
        if math.sqrt((XY[i][0] - XY[j][0]) ** 2 + (XY[i][1] - XY[j][1]) ** 2) > max_num:
            max_num = math.sqrt((XY[i][0] - XY[j][0]) ** 2 + (XY[i][1] - XY[j][1]) ** 2)

print(max_num)