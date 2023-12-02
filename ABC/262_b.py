from collections import defaultdict

n, m = map(int, input().split())

graph_tf = [[False] * n for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    graph_tf[u-1][v-1] = True
    graph_tf[v-1][u-1] = True

count = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if graph_tf[i][j] and graph_tf[j][k] and graph_tf[k][i]:
                count += 1

print(count)