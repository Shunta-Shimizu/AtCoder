from collections import defaultdict, deque
n, k = map(int, input().split())

# medicine = []
# total = 0
# for i in range(n):
#     a, b = map(int, input().split())
#     medicine.append([a, b])
#     total += b

# medicine = sorted(medicine, key=lambda x:x[0])
# # print(medicine)
# # ans = defaultdict(int)
# if total <= k:
#     print(1)
# else:
#     for a, b in medicine:
#         # ans[d] = total
#         total -= b
#         if total <= k:
#             print(a+1)
#             break

medicine = defaultdict(list)
total = 0
for _ in range(n):
    a, b = map(int, input().split())
    medicine[a].append(b)
    total += b

medicine = dict(sorted(medicine.items(), key=lambda x:x[0]))
if total <= k:
    print(1)
    exit()
for d, n_l in medicine.items():
    for m in n_l:
        total -= m
    if total <= k:
        print(d+1)
        break

