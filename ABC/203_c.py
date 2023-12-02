from collections import defaultdict

n, k = map(int, input().split())

Friend = defaultdict(list)
for _ in range(n):
    a, b = map(int, input().split())
    Friend[a].append(b)

Friend = dict(sorted(Friend.items()))

for pi, v in Friend.items():
    if pi > k:
        break
    k += sum(v)

print(k)