from collections import deque
q = int(input())

cylinder = deque()
for _ in range(q):
    query = list(map(int, input().split()))
    n = query[0]
    if n == 1:
        x = query[1]
        c = query[2]
        cylinder.append([x, c])
        # print(cylinder)
    else:
        c = query[1]
        ans = 0
        while cylinder:
            d = cylinder.popleft()
            if d[1] > c:
                ans += d[0]*c
                d[1] -= c
                cylinder.appendleft(d)
                break
            else:
                c -= d[1]
                ans += d[0]*d[1]
        # print(cylinder)
        print(ans)