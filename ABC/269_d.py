from collections import defaultdict
n = int(input())

graph = []
tf = defaultdict(bool)
for _ in range(n):
    x, y = map(int, input().split())
    