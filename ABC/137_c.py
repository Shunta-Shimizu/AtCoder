from collections import defaultdict
n = int(input())
S = []
for _ in range(n):
    s = input()
    S.append(s)

count = defaultdict(int)
for s in S:
    s_sort = tuple(sorted(list(s)))
    count[s_sort] += 1

ans = 0
for v in count.values():
    if v >= 2:
        ans += v*(v-1) // 2

print(ans)