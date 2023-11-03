from collections import deque
q = int(input())
cards = deque()
ans = list()
for i in range(q):
    t, x = map(int, input().split())
    if t == 1:
        cards.appendleft(x)
    elif t == 2:
        cards.append(x)
    else:
        ans.append(cards[x-1])

print(*ans, sep="\n")