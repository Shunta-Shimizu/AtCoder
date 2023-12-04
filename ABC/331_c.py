from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))

count = defaultdict(int)
sumA = sum(A)

for i, a in enumerate(A):
    count[a] += 1

count = dict(sorted(count.items(), key=lambda x:x[0]))
ans = defaultdict(int)
for k, v in count.items():
    sumA -= k*v
    ans[k] = sumA

for a in A:
    print(ans[a], end=" ")