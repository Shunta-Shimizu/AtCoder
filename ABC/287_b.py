n, m = map(int, input().split())

S = []
for _ in range(n):
    s = input()
    S.append(s[-3:])

count = 0
T = set()
for _ in range(m):
    t = input()
    T.add(t)

for s in S:
    if s in T:
        count += 1
        
print(count)
