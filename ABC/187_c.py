n = int(input())

S = []
S_set = set()
for _ in range(n):
    s = input()
    S.append(s)
    S_set.add(s)

for i in range(n):
    if "!" + S[i] in S_set:
        print(S[i])
        exit()
    # elif S[i] in S_set:
    #     print(S[i])
    #     exit()

print("satisfiable")
