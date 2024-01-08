n = int(input())
LR = []
for _ in range(n):
    l, r = map(int, input().split())
    LR.append([l, r])

LR_sort = list(sorted(LR, key=lambda x:x[0]))
ans = []
for i, lr in enumerate(LR_sort):
    if i == 0:
        ans.append(lr)
    else:
        if ans[-1][1] < lr[0]:
            ans.append(lr)
        elif ans[-1][1] ==  lr[0]:
            ans[-1][1] = lr[1]
        elif ans[-1][1] > lr[0]:
            if ans[-1][1] <= lr[1]:
                ans[-1][1] = lr[1]

for a in ans:
    print(*a)