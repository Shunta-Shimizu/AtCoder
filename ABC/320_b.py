S = list(input())

ans = 0
S_l = []
for i in range(len(S)+1):
    for j in range(i):
        S_l.append(S[j:i])

# print(len(S_l))
# print(S_l)
for s in S_l:
    if s == s[::-1]:
        ans = max(ans, len(s))

print(ans)