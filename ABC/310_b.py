n, m = map(int, input().split())

P = []
C = []
F = []
for _ in range(n):
    pcf = list(map(int, input().split()))
    P.append(pcf[0])
    C.append(pcf[1])
    F.append(pcf[2:])

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        else:
            if P[i] >= P[j]:
                tf2 = True
                count = 0
                for fj in F[j]:
                    if fj in F[i]:
                        count += 1
                if count == C[i]:
                    if P[i] > P[j] or C[j] > C[i]:
                        # print(i, j)
                        print("Yes")
                        exit()


print("No")
