S = list(input())

for i in range(len(S)):
    S[i] = "x"

print(*S, sep="")