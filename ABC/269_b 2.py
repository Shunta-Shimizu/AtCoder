S = []
for _ in range(10):
    s = list(input())
    S.append(s)

i_set = set()
j_set = set()

for i in range(10):
    for j in range(10):
        if S[i][j] == "#":
            i_set.add(i)
            j_set.add(j)

sort_iset = sorted(i_set)
sort_jset = sorted(j_set)

print(sort_iset[0]+1, sort_iset[-1]+1)
print(sort_jset[0]+1, sort_jset[-1]+1)
            