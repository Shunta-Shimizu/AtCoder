import math

n, k = map(int, input().split())
A = list(map(int, input().split()))

XY = []
L = []
for i in range(n):
    xy = list(map(int, input().split()))
    XY.append(xy)

ans = []
for xy in XY:
    R = []
    for a in A:
        light_x = XY[a-1][0]
        light_Y = XY[a-1][1]
        r = math.sqrt((xy[0]-light_x)**2 + (xy[1]-light_Y)**2)
        R.append(r)
    ans.append(min(R))
    
print(max(ans))
