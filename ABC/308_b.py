from collections import defaultdict    
n, m = map(int, input().split())
C = list(map(str, input().split()))
D = list(map(str, input().split()))
P = list(map(int, input().split()))

total = 0
price =  defaultdict(int)
for c in C:
    if c not in D:
        price[c] = P[0]
    else:
        price[c] = P[D.index(c)+1]

for c in C:
    total += price[c]

print(total)