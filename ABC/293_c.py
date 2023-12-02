h, w = map(int, input().split())

A = []
for _ in range(h):
    A.append(list(map(int, input().split())))

n = h + w - 2
ans = 0
for bit in range(1 << n):
    now_x = 1
    now_y = 1
    happy = {A[now_x-1][now_y-1]}
    for i in range(n):
        if 1 & (bit >> i) > 0:
            now_x += 1
        else:
            now_y += 1
        if now_x > h or now_y > w:
            break
        else:
            happy.add(A[now_x-1][now_y-1])
    # print(happy)
    if len(happy) == n + 1:
        ans += 1

print(ans)