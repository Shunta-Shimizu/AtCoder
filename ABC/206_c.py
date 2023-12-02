from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))

A_set = set(A)
Info = defaultdict(int)
for a in A:
    Info[a] += 1

ans = n*(n-1)//2
for i in Info.keys():
    if Info[i] == 1:
        continue
    else:
        ans -= (Info[i]*(Info[i]-1)//2)

print(ans)