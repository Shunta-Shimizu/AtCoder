# from collections import deque
# # import queue
# import heapq
# from collections import defaultdict, deque
# q = int(input())
# Query = []
# for i in range(q):
#     query = list(map(int, input().split()))
#     Query.append(query)

# nums = defaultdict(int)
# max_heapq = []
# min_heapq = []

# for query in Query:
#     if query[0] == 1:
#         nums[query[1]] += 1
#         heapq.heappush(max_heapq, -query[1])
#         heapq.heappush(min_heapq,query[1])
#     elif query[0] == 2:
#         nums[query[1]] -= min(query[2], nums[query[1]])
#     elif query[0] == 3:
#         while nums[-max_heapq[0]] == 0:
#             heapq.heappop(max_heapq)

#         while nums[min_heapq[0]] == 0:
#             heapq.heappop(min_heapq)
        
#         print(-max_heapq[0]-min_heapq[0])

# from collections import defaultdict    
# n, m = map(int, input().split())
# C = list(map(str, input().split()))
# D = list(map(str, input().split()))
# P = list(map(int, input().split()))

# total = 0
# price =  defaultdict(int)
# for c in C:
#     if c not in D:
#         price[c] = P[0]
#     else:
#         price[c] = P[D.index(c)+1]

# for c in C:
#     total += price[c]

# print(total)

from collections import defaultdict
from fractions import Fraction
from decimal import Decimal
n = int(input())
AB = []

# A_dict = defaultdict(int)
# B_dict = defaultdict(int)
for i in range(n):
    a, b = map(str, input().split())
    AB.append([a, b])
    # A_dict[i+1] = a
    # B_dict[i+1] = b

P = defaultdict(list)
for i in range(n):
    P[Decimal(AB[i][0]) / (Decimal(AB[i][0])+Decimal(AB[i][1]))].append(i+1)

P = dict(sorted(P.items(), reverse=True, key=lambda x:x[0]))
for k, v in P.items():
    print(*v, end=" ")

# import sys
# sys.setrecursionlimit(10**9)
# h, w = map(int, input().split())
# S = []
# for _ in range(h):
#     S.append(input())

# name = "snuke"
# patern = [[1, 0], [0, 1], [1, 1], [-1, 0], [0, -1], [-1, -1], [1, -1], [-1, 1]]
