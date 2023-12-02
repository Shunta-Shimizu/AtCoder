n, q = map(int, input().split())

# follow = {}
# for i in range(1, n+1):
#     follow[i] = set()

# ans = []
# for _ in range(q):
#     t, a, b = map(int, input().split())

#     if t == 1 and a not in follow[b]:
#         follow[b].add(a)
#     elif t == 2 and b in follow[a]:
#         follow[a].discard(b)
#     elif t == 3:
#         if a in follow[b] and b in follow[a]:
#             ans.append("Yes")
#         else:
#             ans.append("No")

# print(*ans, sep="\n")

follow = set()

ans = []
for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        follow.add((a, b))
    elif t == 2:
        follow.discard((a, b))
    else:
        if (a, b) in follow and (b, a) in follow:
            ans.append("Yes")
        else:
            ans.append("No")

print(*ans, sep="\n")