S = list(input())

S_set = set(S)

if len(S) != len(S_set):
    print("No")
    exit()

c1 = 0
c2 = 0
for s in S:
    if s.istitle():
        c1 += 1
    else:
        c2 += 1

if c1 > 0 and c2 > 0:
    print("Yes")
else:
    print("No")