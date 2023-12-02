import itertools
n, k = map(int, input().split())
T = []
for _ in range(n):
    t = list(map(int, input().split()))
    T.append(t)

l = [i+1 for i in range(1, n)]
city = list(itertools.permutations(l, n-1))

ans = 0
for i in range(len(city)):
    time = 0
    now = 1
    C = city[i]
    for c in C:
        time += T[now-1][c-1]
        now = c
    time += T[C[-1]-1][0]
    if time == k:
        ans += 1

print(ans)