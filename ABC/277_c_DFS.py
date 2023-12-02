from collections import defaultdict
import sys
sys.setrecursionlimit(10**8)

n = int(input())

graph = defaultdict(list)

for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = []
def DFS(now, pre):
    ans.append(now)
    for to in graph[now]:
        if to != pre:
             DFS(to, now)
             ans.append(now)

DFS(1, -1)
print(max(ans))


graph = defaultdict(list)
# 連結成分個数を数える時など
tf = defaultdict()
for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    tf[a] = False
    tf[b] = False 

# グラフの連結を確かめるときなど
# tf = defaultdict(lambda:False)
ans = []
def dfs(now):
    tf[now] = True
    ans.append(now)
    for to in graph[now]:
        if tf[to] == False:
            print(now, to)
            dfs(to)

dfs(1)
# print(tf)
print(max(ans))