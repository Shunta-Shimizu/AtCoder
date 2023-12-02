from collections import defaultdict
n, m = map(int, input().split())
A = []
for _ in range(m):
    a = list(map(int, input().split()))
    A.append(a)

nextP = defaultdict(set)
for i in range(m):
    for j in range(n):
        if j == 0:
            nextP[A[i][j]].add(A[i][j+1])
        elif j == n-1:
            nextP[A[i][j]].add(A[i][j-1])
        else:
            nextP[A[i][j]].add(A[i][j-1])
            nextP[A[i][j]].add(A[i][j+1])

nums = [i+1 for i in range(n)]
ans = set()
for k, v in nextP.items():
    v.add(k)
    flag = True
    for num in nums:
        if num in v:
            continue
        else:
            ans.add((min(k, num), max(k, num)))
print(len(ans))

