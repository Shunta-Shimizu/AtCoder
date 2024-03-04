from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))

idx = defaultdict(int)
for i, a in enumerate(A):
    idx[a] = i+1
    # if i+1 == n:
    #     idx[6] = 10**8

idx = dict(sorted(idx.items(), key=lambda x:x[0]))
# print(idx)
ans = []
pre = 0
for i in range(n):
    if i == 0:
        ans.append(idx[-1])
        pre = idx[-1]
    else:
        ans.append(idx[pre])
        pre = idx[pre]

print(*ans)