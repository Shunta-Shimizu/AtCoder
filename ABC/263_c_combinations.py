# Pythonで提出
import itertools

n, m = map(int, input().split())

ans = itertools.combinations([i+1 for i in range(m)], n)

for a in ans:
    print(*a)