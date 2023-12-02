import itertools

n , k , d = map(int, input().split())
A = list(map(int, input().split()))

comb_num = list(itertools.combinations(range(0, n), k))

ans = []
for comb in comb_num:
    sum = 0
    for i in comb:
        sum += A[i]
    if sum % d == 0:
        ans.append(sum)

if len(ans) == 0:
    print(-1)
else:
    print(max(ans))