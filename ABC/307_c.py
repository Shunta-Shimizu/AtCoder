ha, wa = map(int, input().split())
A = []
for _ in range(ha):
    a = list(input())
    A.append(a)

hb, wb = map(int, input().split())
B = []
for _ in range(hb):
    b = list(input())
    B.append(b)

hx, wx = map(int, input().split())
X = []
for _ in range(hx):
    x = list(input())
    X.append(x)

hc = max(hx, ha, hb)
wc = max(wx, wa, wb)
C = []
D = []
for _ in range(hc):
    c = list("." for _ in range(wc))
    C.append(c)
    D.append(c)

C_org = D
# for _ in range(2):
for i in range(hc):
    for j in range(wc):
        for k in range(ha):
            for l in range(wa):
                C[i][j] = A[k][l]

    print(C)
                    # for x in range(hb):
                    #     for y in range(wb):
                    #         C[i][j] = B[x][y]
            
    # if C[:hx][:wx] == X:
    #     print(C)
    #     print("Yes")
    #     exit()
    # else:
    #     C = C_org

print(C)
print("No")

