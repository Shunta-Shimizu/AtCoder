n = int(input())
S = list(map(int, input().split()))

A = []
for i in range(n):
    if i == 0:
        A.append(S[i])
    else:
        A.append(S[i]-S[i-1])

print(*A, sep=" ")


