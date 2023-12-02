from collections import defaultdict

n = int(input())
S = []
S_set = set()
s_count = defaultdict(lambda:-1)

for _ in range(n):
    s = input()
    S.append(s)
    S_set.add(s)

for s in S:
    if s in S_set:
        s_count[s] += 1
        if s_count[s] == 0:
            print(s)
            continue
        else:
            s = s + "(" + str(s_count[s]) + ")"
            print(s)

