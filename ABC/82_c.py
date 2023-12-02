from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))

count = defaultdict(int)
for a in A:
    count[a] += 1

ans = 0
for k, v in count.items():
    if k == v:
        continue
    elif k > v:
        ans += v
    else:
        ans += v-k

print(ans)