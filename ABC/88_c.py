C = []
for _ in range(3):
    c = list(map(int, input().split()))
    C.append(c)

for i in range(101):
    b1 = C[0][0] - i
    b2 = C[0][1] - i
    b3 = C[0][2] - i
    for j in range(101):
        if b1+j == C[1][0] and b2+j == C[1][1] and b3+j == C[1][2]:
            for k in range(101):
                if b1+k == C[2][0] and b2+k == C[2][1] and b3+k == C[2][2]:
                    print("Yes")
                    exit()

print("No")