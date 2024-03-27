from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))

tf = defaultdict(bool)
f = 0
ans = 0
for i, a in enumerate(A):
    if i+1 != a:
        if i+1-f != a:
            f += 1
        else:
            tf[a] = True
    else:
        if i+1-f != a:
            f += 1
        else:
            if tf[a]:
                f += 1

if len(tf) == 0:
    print(-1)
else:
    print(f)