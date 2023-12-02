n = int(input())

range_set = []
for _ in range(n):
    t, l, r = map(int, input().split())
    if t == 1:
        lr_tuple = (l, r)
    elif t == 2:
        lr_tuple = (l, r-10**(-5))
    elif t == 3:
        lr_tuple = (l+10**(-5), r)
    else:
        lr_tuple = (l+10**(-5), r-10**(-5))
    range_set.append(lr_tuple)

ans = 0
for i in range(n):
    l1 = range_set[i][0]
    r1 = range_set[i][1]
    for j in range(i+1, n):
        l2 = range_set[j][0]
        r2 = range_set[j][1]
        if r1 < l2:
            continue
        elif r2 < l1:
            continue
        else:
            ans += 1

print(ans)

