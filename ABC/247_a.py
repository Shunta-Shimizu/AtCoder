S = list(input())

ans = "0"
for i in range(1, len(S)):
    if S[i-1] == "0":
        ans += "0"
    else:
        ans += "1"

print(ans)
