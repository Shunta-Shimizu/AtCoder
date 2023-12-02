n, m = map(int, input().split())

S = []
Pair = []
for i in range(2*n):
    S.append(list(input()))
    Pair.append([0, i])

def judge(a, b):
    if a == b:
        return -1
    elif a == "G" and b == "C":
        return 0
    elif a == "C" and b == "P":
        return 0
    elif a == "P" and b == "G":
        return 0
    return 1

for j in range(m):
    for i in range(n):
        p1 = Pair[2*i][1]
        p2 = Pair[2*i+1][1]
        result = judge(S[p1][j], S[p2][j])
        if result != -1:
            Pair[2*i+result][0] -= 1
    Pair.sort()

for _, i in Pair:
    print(i+1)


