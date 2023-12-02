from collections import defaultdict
n = int(input())
S_dict = defaultdict(int)

for _ in range(n):
    s = input()
    S_dict[s] += 1

S_dict = dict(sorted(S_dict.items(), key=lambda x:x[1], reverse=True))
max_count = list(S_dict.items())[0][1]
ans = []
for k, v in S_dict.items():
    if v == max_count:
        ans.append(k)

ans.sort()
for a in ans:
    print(a)