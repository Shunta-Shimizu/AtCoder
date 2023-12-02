from collections import defaultdict
n = int(input())
A = []
for _ in range(n):
    c = int(input())
    a = list(map(int, input().split()))
    A.append(a)

x = int(input())

count = defaultdict(list)
for i in range(n):
    if x in A[i]:
        count[len(A[i])].append(i+1)

count = dict(sorted(count.items(), key=lambda x:x[0]))

if len(count) == 0:
    print(0)
    print("")
else:
    print(len(list(count.values())[0]))
    print(*sorted(list(count.values())[0]))