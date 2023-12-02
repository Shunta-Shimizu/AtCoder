n, q = map(int, input().split())

follow = set()
check = []
for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        follow.add((a, b))
    elif t == 2:
        if (a, b) in follow:
            follow.remove((a, b))
    else:
        if (a, b) in follow and (b, a) in follow:
            check.append("Yes")
        else:
            check.append("No")

print(*check, sep="\n")
