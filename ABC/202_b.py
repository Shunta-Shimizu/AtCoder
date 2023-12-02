S = list(input())

S_reverse = list((reversed(S)))

for i in range(len(S_reverse)):
    if S_reverse[i] == "6":
        S_reverse[i] = "9"
    elif S_reverse[i] == "9":
        S_reverse[i] = "6"

print(*S_reverse, sep="")