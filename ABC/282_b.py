n, m = map(int, input().split())

S = []
for _ in range(n):
    s = list(input())
    S.append(s)

for i in range(n):
    for j in range(m):
        if S[i][j] == "o":
            S[i][j] = 1
        else:
            S[i][j] = 0

count = 0
for i in range(n):
    for j in range(i, n):
        t = [max(t) for t in zip(S[i], S[j])]
        if t == [1] * m and i != j:
            count += 1

print(count)

# count = 0
# pair = 0
# for i in range(n):
#     for j in range(i+1, n):
#         for k in range(m):
#             if S[i][k] == "x" and S[j][k] == "x":
#                 break
#             else:
#                 count += 1
#         if count == m:
#             pair += 1
#         count = 0

# print(pair)