from collections import defaultdict
import string
n = int(input())
S = input()
q = int(input())

p = defaultdict(str)
for s in string.ascii_lowercase:
    p[s] = s 

for _ in range(q):
    c, d = map(str, input().split())
    for k, v in p.items():
        if v == c:
            p[k] = d

ans = ""
for s in S:
    ans += p[s]

print(ans)