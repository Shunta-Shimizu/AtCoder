n = int(input())
AB = []
for _ in range(n):
    a, b = map(int, input().split())
    AB.append([a, b, b-a])

AB = sorted(AB, key=lambda x:x[2])
# print(AB)
ans = 0
for i in range(n):
    if i == n-1:
        ans += AB[i][1]
    else:
        ans += AB[i][0]

print(ans)