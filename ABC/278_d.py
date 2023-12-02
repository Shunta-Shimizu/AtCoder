n = int(input())
A = list(map(int, input().split()))
q = int(input())

# ans = []
# for _ in range(q):
#     Query = list(map(int, input().split()))
#     if len(Query) < 3:
#         if Query[0] == 1:
#             A = list(map(lambda a:Query[1], A))
#         else:
#             ans.append(A[Query[1]-1])
#     else:
#         A[Query[1]-1] = A[Query[1]-1] + Query[2]
#         # print(A)

# print(*ans, sep="\n")

from collections import defaultdict

diff = defaultdict(int)
g = 0
base = 0

for _ in range(q):
    Query = list(map(int, input().split()))
    if Query[0] == 1:
        g += 1
        base = Query[1]
    elif Query[0] == 2:
        diff[(g, Query[1])] += Query[2]
    else:
        if g > 0:
            print(base + diff[(g, Query[1])])
        else:
            print(A[Query[1]-1] + diff[(g, Query[1])])
