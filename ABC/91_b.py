from collections import defaultdict
n = int(input())
S = []
blue = defaultdict(int)
red = defaultdict(int)
for _ in range(n):
    s = input()
    S.append(s)
    blue[s] += 1
    red[s] = 0
m = int(input())
T = []
for _ in range(m):
    t = input()
    T.append(t)
    red[t] += 1

ans = 0
for k, v in blue.items():
    ans = max(ans, blue[k]-red[k])

print(ans)