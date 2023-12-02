n = int(input())

S = []
T = []
for _ in range(n):
    s, t = map(str, input().split())
    S.append(s)
    T.append(int(t))

max = -1
max_idx = -1
handed_poem = set()
for i in range(n):
    if S[i] in handed_poem:
        continue
    else:
        if T[i] > max:
            max = T[i]
            max_idx = i
    handed_poem.add(S[i])

print(max_idx + 1)