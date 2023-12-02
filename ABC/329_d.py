from collections import defaultdict
n, m = map(int, input().split())
A = list(map(int, input().split()))

count = defaultdict(int)
max_v = 0
max_num = 0
ans = []
for i, a in enumerate(A):
    if i == 0:
        count[a] += 1
        max_v = a
        max_num = count[a]
        ans.append(max_v)
    else:
        count[a] += 1
        if max_num == count[a]:
            max_v = min(max_v, a)
            ans.append(max_v)
        elif max_num < count[a]:
            max_v = a
            max_num = count[a]
            ans.append(max_v)
        else:
            ans.append(max_v)

for a in ans:
    print(a)

        