n, m = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
count = []
pre = 0
for i, a in enumerate(A):
    if a-pre > 1:
        count.append(a-pre-1)
        pre = a
    else:
        pre = a

if n-pre > 1:
    count.append(n-pre)
# print(count)
if m == 0:
    print(1)
else:
    if len(count) == 0:
        print(0)
    else:
        min_c = min(count)
        ans = 0
        for ci in count:
            if ci%min_c == 0:
                ans += ci//min_c
            else:
                ans += ci//min_c
                ans += 1
        print(ans)