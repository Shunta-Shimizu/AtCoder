h, w = map(int, input().split())
S = []
for i in range(h):
    s = list(input())
    S.append(s)

for i in range(h):
    for j in range(w-1):
        if S[i][j] == "T" and S[i][j+1] == "T":
            S[i][j] = "P"
            S[i][j+1] = "C"

for s in S:
    print(*s, sep="")