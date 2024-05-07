S = list(input())
T = list(input())

ans = []
si = 0
ti = 0
for i in range(len(T)):
    if S[si] != T[i]:
        continue
    else:
        ans.append(i+1)
        si += 1

print(*ans)