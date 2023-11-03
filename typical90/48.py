n, k = map(int, input().split())
AB = []
for i in range(n):
    a, b = map(int, input().split())
    AB.append(b)
    AB.append(a-b)

AB_sort = list(sorted(AB, reverse=True))
ans = 0
for i in range(k):
    ans += AB_sort[i]

print(ans)