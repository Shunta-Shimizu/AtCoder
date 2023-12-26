from collections import defaultdict
n = int(input())
S = list(input())
q = int(input())

query = defaultdict(list)
type_i = -1
type_t = -1
for i in range(q):
    t, x, c = map(str, input().split())
    t = int(t)
    x = int(x)

    if t == 1:
        query[i] = [t, x, c]
    elif t == 2:
        type_t = 2
        type_i = i
    else:
        type_t = 3
        type_i = i

if type_t != -1:
    for i, s in enumerate(S):
        if type_t == 2:
            S[i] = s.lower()
        else:
            S[i] = s.upper()

    for k, v in query.items():
        if k < type_i:
            if type_t == 2:
                S[v[1]-1] = v[2].lower()
            else:
                S[v[1]-1] = v[2].upper()
        else:
            S[v[1]-1] = v[2]

else:
    for k, v in query.items():
        S[v[1]-1] = v[2]

print(*S, sep="")