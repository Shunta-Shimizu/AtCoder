import itertools
n, m = map(int, input().split())

S = []
for _ in range(n):
    s =  input()
    S.append(s)

S_p = list(itertools.permutations(S, n))

for sp in S_p:
    ans = []
    for i in range(n-1):
        w_s = 0
        for j in range(m):
            if sp[i][j] == sp[i+1][j]:
                continue
            else:
                w_s += 1
        if w_s <= 1:
            ans.append(w_s)
    
    if len(ans) == n-1:
        print("Yes")
        exit()

print("No")
 