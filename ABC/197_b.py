h, w, x, y = map(int, input().split())

S = []
for _ in range(h):
    s = input()
    S.append(s)

ans = 0
for i in range(x-1, -1, -1):
    if S[i][y-1] == "#":
        break
    else:
        ans += 1

for j in range(x-1, h):
    if S[j][y-1] == "#":
        break
    else:
        ans += 1

for k in range(y-1, -1, -1):
    if S[x-1][k] == "#":
        break
    else:
        ans += 1

for l in range(y-1, w):
    if S[x-1][l] == "#":
        break
    else:
        ans += 1

print(ans - 3)
# ans = 0
# count = 0
# tf_x = True
# for i in range(h):
#     if i < x - 1:
#         if S[i][y-1] == ".":
#             count += 1
#         else:
#             count = 0
#     elif i == x - 1:
#         ans += count + 1
#         count = 0
#     else:
#         if S[i][y-1] == "." and tf_x:
#             count += 1
#         else:
#             tf_x = False

# ans += count
# count = 0
# tf_y = True
# for j in range(w):
#     if j < y - 1:
#         if S[x-1][j] == ".":
#             count += 1
#         else:
#             count = 0
#     elif j == y - 1:
#         ans += count
#         count = 0
#     else:
#         if S[x-1][j] == "." and tf_y:
#             count += 1
#         else:
#             tf_y = False

# ans += count

# print(ans)