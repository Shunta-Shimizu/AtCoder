from collections import deque
S = deque(input())
q = int(input())

count = 0
for _ in range(q):
    Query = list(map(str, input().split()))
    t = int(Query[0])
    if t == 1:
        count += 1
    else:
        f = int(Query[1])
        c = Query[2]
        if count%2 == 0:
            if f == 1:
                S.appendleft(c)
            else:
                S.append(c)
        else:
            if f == 1:
                S.append(c)
            else:
                S.appendleft(c)            

if count%2 == 0:
    print(*list(S), sep="")
else:
    print(*list(reversed(list(S))), sep="")