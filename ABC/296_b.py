S = []
for _ in range(8):
    s = list(input())
    S.append(s)

ABC = "abcdefgh"
num = "87654321"
for i in range(8):
    for j in range(8):
        if S[i][j] == "*":
            print(ABC[j]+num[i])

