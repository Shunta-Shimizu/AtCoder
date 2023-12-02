from collections import defaultdict
n, d = map(int, input().split())
S = []
for _ in range(n):
    s = input()
    S.append(s)

ans = []
for i in range(d):
    count = 0
    for j in range(n):
        if S[j][i] == "x":
            continue
        else:
            count += 1
    if count == n:
        ans.append(i)

if len(ans) == 0:
    print(0)
    exit()
elif len(ans) == 1:
    print(1)
    exit()

tmp = ans[0]
c = 1
out = 0
for i in range(1, len(ans)):
    if tmp+1 == ans[i]:
        c += 1
        tmp = ans[i]
        if i == len(ans)-1:
            out = max(out, c)
    else:
        out = max(out, c)
        c = 1
        tmp = ans[i]

print(out)
