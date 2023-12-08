n = int(input())
A = list(map(int, input().split()))

count = []
ans = 0
for i, a in enumerate(A):
    ans += 1
    if i == 0:
        pre = a
        count.append([a, 1])
    else:
        if pre == a:
            count[-1][1] += 1
            if count[-1][1] == a:
                count_pop = count.pop()
                ans -= count_pop[1]
                if len(count) == 0:
                    ans = 0
                    pre = 0
                else:
                    pre = count[-1][0]
        else:
            count.append([a, 1])
            pre = a
    
    print(ans)