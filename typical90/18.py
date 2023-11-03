import math
t = int(input())
l, x, y = map(int, input().split())
q = int(input())
E = []
for _ in range(q):
    e = int(input())
    E.append(e)

for i in range(q):
    theta = E[i] / t * 2 * math.pi
    now = [0, -l/2*math.sin(theta), l/2-l/2*math.cos(theta)]
    dist = math.sqrt((x-now[0])**2 + (y-now[1])**2)
    ans = math.atan(now[2]/dist) / math.pi * 180
    print(ans)