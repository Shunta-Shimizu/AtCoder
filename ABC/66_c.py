from collections import deque
n = int(input())
A = list(map(int, input().split()))

que = deque()
for i in range(n):
    if (i+1)%2 == 1:
        que.append(A[i])
    else:
        que.appendleft(A[i])

if n%2 == 0:
    ans = list(que)
else:
    ans = list(reversed(list(que)))

print(*ans)