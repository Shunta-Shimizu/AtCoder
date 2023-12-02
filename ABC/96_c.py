h, w = map(int, input().split())
S = []
for i in range(h):
    s = list(input())
    S.append(s)

tf = [[False for _ in range(w)] for _ in range(h)]
for i in range(h-1):
    for j in range(w-1):
        if S[i][j] == "#":
            if S[i][j+1] == "#":
                tf[i][j+1] = True
            if S[i+1][j] == "#":
                tf[i+1][j] = True
            if S[i][j+1] != "#" and S[i+1][j] != "#":
                if tf[i][j] == True:
                    continue
                else:
                    print("No")
                    exit()

# print(tf)
print("Yes")