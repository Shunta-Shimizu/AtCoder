from collections import deque
n, q = map(int, input().split())
A = list(map(int, input().split()))

que = deque(A)
ans = []
for i in range(q):
    t, x, y = map(int, input().split())
    if t == 1:
        tmp = que[x-1]
        que[x-1] = que[y-1]
        que[y-1] = tmp
    elif t == 2:
        tmp = que.pop()
        que.appendleft(tmp)
    else:
        ans.append(que[x-1])

print(*ans, sep="\n")