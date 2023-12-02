from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))

count = defaultdict(int)
ans = []
for i in range(len(A)):
    count[A[i]] += 1
    if count[A[i]] == 2:
        ans.append([A[i], i+1])

for i in range(len(ans)):
    print(ans[i][0], end=" ")