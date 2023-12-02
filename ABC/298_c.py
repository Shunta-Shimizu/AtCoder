from collections import defaultdict
import bisect
n = int(input())
q = int(input())

cards = defaultdict(list)
boxes = defaultdict(set)
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        cards[query[2]].append(query[1])
        boxes[query[1]].add(query[2])
    elif query[0] == 2:
        print(*sorted(cards[query[1]]), sep= " ")
    else:
        print(*sorted(boxes[query[1]]), sep=" ")
