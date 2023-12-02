from collections import defaultdict
n = int(input())
SP_l = []
SP = defaultdict(list)
for _ in range(n):
    s, p = map(str, input().split())
    SP_l.append([s, int(p)])
    SP[s].append(int(p))

SP_sort = dict(sorted(SP.items(), key=lambda x:x[0]))
for s, p in SP_sort.items():
    p.sort(reverse=True)
    for pi in p:
        print(SP_l.index([s, pi])+1)