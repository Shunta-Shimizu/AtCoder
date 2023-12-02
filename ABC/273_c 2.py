from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))
A_sort = sorted(A, reverse=True)
A_set = sorted(list(set(A)), reverse=True)

count = defaultdict(int)
for a in A:
    count[a] += 1

m = len(A_set)
i = 0
for a in A_set:
    print(count[a])
for i in range(0, n-m):
    print(0)