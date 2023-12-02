from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))

ans = A
insert_num = defaultdict(list)
for i in range(n-1):
    if A[i+1] - A[i] > 1:
        for j in range(1, A[i+1]-A[i]):
            insert_num[i+1].append(A[i]+j)
    elif A[i+1] - A[i] < -1:
        for j in range(1, abs(A[i+1]-A[i])):
            insert_num[i+1].append(A[i]-j)

count = 0
for k, v in insert_num.items():
    for i in range(len(v)):
        ans.insert(k+i+count, v[i])
    count += len(v)

print(*ans)
