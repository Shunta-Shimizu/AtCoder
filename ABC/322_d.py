from collections import defaultdict
P = []
for i in range(12):
    if i % 4 == 0:
        P.append([])
    p = list(input())
    P[i//4].append(p)

ans = [["#" for _ in range(4)] for _ in range(3)]

P1 = []
for i in range(4):
    if "#" in P[0][i]:
        P1.append(P[0][i]) 

P1 = list(map(list, (zip(*P1))))
P1_t = []
for j in range(len(P1)):
    if "#" in P1[j]:
        P1_t.append(P1[j])
P1 = list(map(list, (zip(*P1_t))))


P2 = []
for i in range(4):
    if "#" in P[1][i]:
        P2.append(P[1][i]) 
P2 = list(map(list, (zip(*P2))))
P2_t = []
for j in range(len(P2)):
    if "#" in P2[j]:
        P2_t.append(P2[j])
P2 = list(map(list, (zip(*P2_t))))


P3 = []
for i in range(4):
    if "#" in P[2][i]:
        P3.append(P[2][i]) 

P3 = list(map(list, (zip(*P3))))
P3_t = []
for j in range(len(P3)):
    if "#" in P3[j]:
        P3_t.append(P3[j])
P3 = list(map(list, (zip(*P3_t))))

pos = defaultdict(int)
pos["P1"] = len(P1)*len(P1_t)
pos["P2"] = len(P2)*len(P2_t)
pos["P3"] = len(P3)*len(P3_t)

pos = dict(sorted(pos.items(), key=lambda x:x[1]))

P1_rotate = list(zip(*P1[::-1]))
print(P1_rotate)
P1_rotate = list(zip(*P1_rotate[::-1]))
print(P1_rotate)