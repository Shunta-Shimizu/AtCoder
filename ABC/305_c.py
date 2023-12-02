from collections import defaultdict
h, w = map(int, input().split())
S = []
count = defaultdict(list)
S_short = []
for i in range(h):
    s = list(input())
    if s.count("#") != 0:
        count[s.count("#")].append(i)
        S_short.append(s)
    S.append(s)

key_min = sorted(list(count.keys()))
# print(key_min)
# print(count)
ans_h = 0
ans_w= 0
for c, idx_l in count.items():
    if len(idx_l) == 1 and c == key_min[0]:
        ans_h = idx_l[0]
        break

short_h = S_short.index(S[ans_h])
if short_h-1 < 0:
    for j in range(w):
        if S_short[short_h][j] != S_short[short_h+1][j]:
            ans_w = j
elif short_h+1 >= len(S_short):
    for j in range(w):
        if S_short[short_h][j] != S_short[short_h-1][j]:
            ans_w = j
else:
    for j in range(w):
        if S_short[short_h][j] != S_short[short_h-1][j] or S_short[short_h][j] != S_short[short_h+1][j]:
            ans_w = j

print(ans_h+1, ans_w+1)
