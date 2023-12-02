from collections import deque
n = int(input())
A = list(map(int, input().split()))

que = deque()
for i in range(n):
    if i % 2 == 0:
        que.appendleft(A[i])
    else:
        que.append(A[i])

if n%2 == 0:
    print(*list(reversed(que)), sep=" ")
else:
    print(*que, sep=" ")