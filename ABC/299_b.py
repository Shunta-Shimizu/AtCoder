from collections import defaultdict

n, t = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

card = defaultdict(list)
CR = []
for i in range(n):
    card[C[i]].append(R[i])
    CR.append([C[i], R[i]])

max_r = 0
if len(card[t]) >= 1:
    max_r = max(card[t])
    ans = CR.index([t, max_r]) + 1
else:
    max_r = max(card[CR[0][0]])
    ans = CR.index([CR[0][0], max_r]) + 1

print(ans)



