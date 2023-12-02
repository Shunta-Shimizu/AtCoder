from collections import defaultdict
X = list(input())
n = int(input())
S = []
for _ in range(n):
    S.append(input())

x_index = defaultdict(int)
for i in range(len(X)):
    x_index[X[i]] = i

s_replace = defaultdict(str)
ABC = "abcdefghijklmnopqrstuvwxyz"
for i in range(n):
    s_replace[S[i]] = ""
    for j in range(len(S[i])):
        s_replace[S[i]] += ABC[x_index[S[i][j]]]

s_replace = dict(sorted(s_replace.items(), key=lambda x:x[1]))

for k, v in s_replace.items():
    print(k)