a, b = map(int, input().split())

ans = 0
cnt = 0
if b == 1:
    ans = 0
else:
    while cnt < b:
        if ans >= 1:
            cnt -= 1
            cnt += a
        else:
            cnt += a
        ans += 1

print(ans)