from collections import defaultdict
S = input()
count  = defaultdict(int)
for s in S:
    count[s] += 1

count = dict(sorted(count.items(), key=lambda x:x[1], reverse=True))
ans = []
i = 0
for k, v in count.items():
    if i == 0:
        ans.append(k)
        pre = v
        i += 1
    else:
        if pre == v:
            ans.append(k)

ans.sort()
print(ans[0])
