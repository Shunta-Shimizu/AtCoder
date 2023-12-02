S = input()

word = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n = len(S)
ans = 0
for i in range(n):
    ans += 26**(n-i-1) * (word.index(S[i])+1)

print(ans)