from collections import defaultdict
n = int(input())
FS = []
fs = defaultdict(list)
for _ in range(n):
    f, s = map(int, input().split())
    FS.append([f, s])

FS_sort = sorted(FS, key=lambda x:x[1], reverse=True)
# print(FS_sort)
max_s = FS_sort[0][1]
smax_s = 0
fs[FS_sort[0][0]].append(max_s)
for i in range(n-1):
    if FS_sort[0][0] != FS_sort[i+1][0]:
        smax_s = max(smax_s, FS_sort[i+1][1])
    if len(fs[FS_sort[i+1][0]]) <= 2:
        fs[FS_sort[i+1][0]].append(FS_sort[i+1][1])

# print(max_s, smax_s)
ans = max_s + smax_s
# print(ans)
# print(fs)
for k, v in fs.items():
    if len(v) < 2:
        continue
    ans = max(ans, v[0]+v[1]//2)

print(ans)