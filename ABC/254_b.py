n = int(input())

ans = []
for i in range(n):
    ans.append([])
    for j in range(i+1):
        if j == 0 or j == i:
            ans[i].append(1)
        else:
            ans[i].append(ans[i-1][j-1]+ans[i-1][j])

for a in ans:
    print(*a)