h, w = map(int, input().split())

A = []
for _ in range(h):
    A.append(list(map(int, input().split())))

ans = []
ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(h):
    S = ""
    for j in range(w):
        if A[i][j] == 0:
            S += "."
        else:
            S += ABC[A[i][j]-1]
    ans.append(S)

for s in ans:
    print(s)
