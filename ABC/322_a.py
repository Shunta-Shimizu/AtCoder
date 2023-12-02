n = int(input())
s = list(input())
ans = []
for i in range(n):
    ans.append(s[i])
    if len(ans) >= 3:
        if ans[i-2:i+1] == ["A", "B", "C"]:
            print(i-2+1)
            exit()
print(-1)