n, m = map(int, input().split())
AB = []
for _ in range(n):
    a, b = map(int, input().split())
    AB.append([a, b])

CD = []
for _ in range(m):
    c, d = map(int, input().split())
    CD.append([c, d])

ans = []
for i in range(n):
    cp = [-1, 10**9]
    for j in range(m):
        if abs(AB[i][0]-CD[j][0]) + abs(AB[i][1]-CD[j][1]) < cp[1]:
            cp = [j+1, abs(AB[i][0]-CD[j][0]) + abs(AB[i][1]-CD[j][1])]

    print(cp[0])