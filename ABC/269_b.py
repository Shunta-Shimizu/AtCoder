S = []
for i in range(10):
    s = list(map(str, input()))
    S.append(s)

i_list = []
j_list = []
for i in range(10):
    for j in range(10):
        if S[i][j] == "#":
            i_list.append(i)
            j_list.append(j)

print(i_list[0]+1, i_list[-1]+1)
print(j_list[0]+1, j_list[-1]+1)