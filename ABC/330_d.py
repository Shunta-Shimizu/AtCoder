from collections import defaultdict
n = int(input())
S = []
count_i = defaultdict(set)
count_j = defaultdict(set)
for i in range(n):
    s = input()
    for j in range(len(s)):
        if s[j] == "o":
            count_i[i].add(j)
            count_j[j].add(i)

ans = 0
for i in list(count_i.keys()):
    if len(count_i[i]) < 2:
        continue
    else:
        total = 0
        for j in count_i[i]:
            total += len(count_j[j])-1
        ans += total*(len(count_i[i])-1) 

print(ans)
