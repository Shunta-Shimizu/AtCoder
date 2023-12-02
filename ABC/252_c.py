from collections import defaultdict
n = int(input())
S = []
for _ in range(n):
    s = list(input())
    S.append(s)

time = defaultdict(set)
for i in range(n):
    for j in range(10):
        t = j
        if t in time[S[i][j]]:
            while True:
                t += 10
                if t not in time[S[i][j]]:
                    break
            time[S[i][j]].add(t)
        else:
            time[S[i][j]].add(t)

ans = 10**8
for k, v in time.items():
    ans = min(ans, max(v))

print(ans)