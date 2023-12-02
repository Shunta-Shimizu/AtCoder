from collections import defaultdict
n, k = map(int, input().split())
S = []
for _ in range(n):
    s = input()
    S.append(s)

ans = 0
for bit in range(1 << n):
    selected_s = []
    for i in range(n):
        if 1 & (bit >> i) > 0:
            selected_s.append(S[i])
        else:
            continue
    
    count_s = defaultdict(int)
    for ss in selected_s:
        for ssi in ss:
            count_s[ssi] += 1
    
    count = 0
    for v in count_s.values():
        if v == k:
            count += 1
    
    ans = max(ans, count)

print(ans)