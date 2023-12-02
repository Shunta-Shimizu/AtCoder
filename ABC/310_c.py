from collections import defaultdict
n = int(input())
S = set()
for _ in range(n):
    s = input()
    s_reverse = s[::-1]
    if s in S or s_reverse in S:
        continue
    else:
        S.add(s)

print(len(S))