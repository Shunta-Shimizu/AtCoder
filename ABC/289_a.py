S = list(input())

for i in range(len(S)):
    if S[i] == "0":
        S[i] = "1"
    else:
        S[i] = "0"

print(*S, sep="")