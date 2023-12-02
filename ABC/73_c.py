from collections import defaultdict
n = int(input())
tf = defaultdict(bool)

for i in range(n):
    a = int(input())
    if tf[a]:
        tf[a] = False
    else:
        tf[a] = True

ans = 0
for k, v in tf.items():
    if v:
        ans += 1

print(ans)
        