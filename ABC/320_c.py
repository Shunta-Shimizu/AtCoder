import itertools

m = int(input())
S = []
for _ in range(3):
    s = input()
    s += s * 2
    S.append(s)

P = list(itertools.permutations(range(3), 3))
ans = 10**9
for p in P:
    for i, r1 in enumerate(S[p[0]]):
        for j, r2 in enumerate(S[p[1]]):
            if i < j and r1 == r2:
                for k, r3 in enumerate(S[p[2]]):
                    if i < j < k and r1 == r2 == r3:
                        ans = min(ans, k)

if ans == 10**9:
    print(-1)
else:
    print(ans)