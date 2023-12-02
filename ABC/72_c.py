from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))

count = defaultdict(int)
for i in range(n):
    count[A[i]-1] += 1
    count[A[i]+1] += 1
    count[A[i]] += 1

count = sorted(count.items(), key=lambda x:x[1], reverse=True)
# print(count)
print(count[0][1])
