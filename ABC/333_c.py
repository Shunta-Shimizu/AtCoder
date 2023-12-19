import itertools
from collections import defaultdict
n = int(input())

nums = []
a = 0
for i in range(12):
    a += 10**i
    nums.append(a)

pair = list(itertools.product(nums, repeat=3))
ans = set()
for p in pair:
    ans.add(sum(p))

ans = list(ans)
ans.sort()
print(ans[n-1])