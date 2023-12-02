from collections import defaultdict, deque
n, m = map(int, input().split())
A = deque(map(int, input().split()))

tmp = A.popleft()
for i in range(n):
    if i+1 == tmp:
        print(0)
        if len(A) == 0:
            exit()
        else:
            tmp = A.popleft()
    else:
        print(tmp-(i+1))

