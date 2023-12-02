S = list(input())
T = list(input())

ABC = "abcdefghijklmnopqrstuvwxyz"
S_index = []
for s in S:
    S_index.append(ABC.index(s))

for i in range(26):
    Ans = []
    for j in S_index:
        j = (i + j) % 26
        Ans.append(ABC[j])
    if Ans == T:
        print("Yes")
        exit()

print("No")
        

    