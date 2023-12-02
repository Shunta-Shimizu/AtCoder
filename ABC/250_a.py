h, w = map(int, input().split())
r, c = map(int, input().split())

ans = 0
for i in range(h):
    for j in range(w):
        if abs(i-(r-1)) + abs(j-(c-1)) == 1:
            ans += 1

print(ans)