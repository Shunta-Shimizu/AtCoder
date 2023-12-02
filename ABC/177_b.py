S = list(input())
T = list(input())

C = []
for i in range(len(S) - len(T) + 1):
    count = 0
    k = 0
    for j in range(i, i+len(T)):
        if S[j] == T[k]:
            count += 1
        k += 1
    C.append(count)

ans = len(T) - max(C)
print(ans)