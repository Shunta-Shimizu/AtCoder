n = int(input())
S = list(input())

ans = 0
for i in range(n-2):
    if S[i] == "A" and S[i+1] == "B" and S[i+2] == "C":
        ans += 1

print(ans)


