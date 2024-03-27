from collections import deque
k, x = map(int, input().split())

que = deque()
que.append(x)
for i in range(1, k):
    que.appendleft(x-i)
    que.append(x+i)

print(*list(que))