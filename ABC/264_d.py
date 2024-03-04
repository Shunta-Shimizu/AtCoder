S = list(input())

A = ["a", "t", "c", "o", "d", "e", "r"]
Si = []
for i, s in enumerate(S):
    Si.append(A.index(s))

count = 0
for i in range(len(Si)):
    for j in range(len(Si)-i-1):
        if Si[j] > Si[j+1]:
            tmp = Si[j]
            Si[j] = Si[j+1]
            Si[j+1] = tmp
            count += 1

print(count)