n = int(input())
S = list(input())

ans = -1
count = 0
for i in range(n):
    if S[i] == "o":
        count += 1
        ans = max(ans, count)
    else:
        count = 0

if ans == n:
    print(-1)
else:
    print(ans)