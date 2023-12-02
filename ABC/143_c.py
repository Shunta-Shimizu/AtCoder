n = int(input())
S = list(input())

ans = S[0]
for i in range(1, n):
    if S[i] != S[i-1]:
        ans += S[i]

print(len(ans))