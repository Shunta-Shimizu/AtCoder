from collections import defaultdict
n = int(input())
AB = []

for i in range(n):
    a, b = map(int, input().split())
    AB.append([a, b])


P = defaultdict(list)
for i in range(n):
    P[AB[i][0] * 10**20 // (AB[i][0]+AB[i][1])].append(i+1)

P = dict(sorted(P.items(), reverse=True, key=lambda x:x[0]))
for k, v in P.items():
    print(*v, end=" ")