from collections import defaultdict
n = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

have = defaultdict(int)
t = 0
for i in range(1, 2*n):
    t = min(T[i%n], t+S[(i-1)%n])
    have[i%n] = t

have = dict(sorted(have.items(), key=lambda x:x[0]))

for k, v in have.items():
    print(v)