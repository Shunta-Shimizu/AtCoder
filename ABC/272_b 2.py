n, m = map(int, input().split())

import itertools

comb = set()
for _ in range(m):
    A = tuple(map(int, input().split()))
    pair = itertools.combinations(A[1:], 2)
    for p in pair:
        comb.add(p)

full_pair = list(itertools.combinations(range(1, n+1), 2))

if len(comb) == len(full_pair):
    print("Yes")
else:
    print("No")