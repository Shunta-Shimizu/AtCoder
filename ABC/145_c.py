import itertools, math
n = int(input())
XY = []
for _ in range(n):
    x, y = map(int, input().split())
    XY.append((x, y))

Ways = list(itertools.permutations([i for i in range(n)]))

ans = 0
for way in Ways:
    dst = 0
    for i in range(1, len(way)):
        dst += math.sqrt((XY[way[i-1]][0]-XY[way[i]][0])**2 + (XY[way[i-1]][1]-XY[way[i]][1])**2)
    ans += dst

print(ans/len(Ways))
