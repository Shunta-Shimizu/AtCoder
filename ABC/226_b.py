from collections import defaultdict
n = int(input())

Ans = defaultdict(set)
for _ in range(n):
    LA = list(map(int, input().split()))
    l = LA[0]
    A = tuple(LA[1:])
    Ans[l].add(A)

ans = 0
for key in Ans.keys():
    ans += len(Ans[key])

print(ans)