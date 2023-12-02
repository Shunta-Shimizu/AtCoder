n = int(input())

S = []
for _ in range(n):
    s = input()
    S.append(s)

print(*list(reversed(S)), sep="\n")