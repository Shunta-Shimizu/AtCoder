# https://atcoder.jp/contests/atc001/tasks/dfs_a

import sys
sys.setrecursionlimit(10**8)

h, w = map(int, input().split())

# map = []
# for i in range(h):
#     C = list(input())
#     if "s" in C:
#         sj = C.index("s")
#         si = i
#     map.append(C)

map = [list(input()) for _ in range(h)]

for j in range(h):
    for i in range(w):
        if map[j][i] == "s":
            sj, si = j, i

def DFS(j, i):
    if j < 0 or j >= h or i < 0 or i >= w or map[j][i] == "#":
        return 
    
    if map[j][i] == "g":
        print("Yes")
        exit()
    
    map[j][i] = "#"

    DFS(j+1, i)
    DFS(j-1, i)
    DFS(j, i+1)
    DFS(j, i-1)

DFS(sj, si)
print("No")







