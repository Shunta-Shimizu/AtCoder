from collections import defaultdict
n, q = map(int, input().split())
A = list(map(int, input().split()))

index_dict = defaultdict(list)
for i in range(n):
    index_dict[A[i]].append(i+1)

for _ in range(q):
    x, k = map(int, input().split())
    if k > len(index_dict[x]):
        print(-1)
    else:
        print(index_dict[x][k-1])

