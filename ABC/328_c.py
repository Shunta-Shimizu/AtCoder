n, q = map(int, input().split())
S = input()

count = [0 for _ in range(n)]
c = 0
for i, si in enumerate(S):
    if i == 0:
        sf = si
        count[i] = c
    else:
        if si == sf:
            c += 1
            count[i] = c
            sf = si
        else:
            sf = si
            count[i] = c

for _ in range(q):
    l, r = map(int, input().split())
    ans = count[r-1]-count[l-1]
    print(ans)