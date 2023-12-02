from collections import defaultdict
n, q = map(int, input().split())

card = defaultdict(int)
for _ in range(q):
    c, x = map(int, input().split())
    if c == 1:
        card[x] += 1
    elif c == 2:
        card[x] = 2
    else:
        if card[x] >= 2:
            print("Yes")
        else:
            print("No")
