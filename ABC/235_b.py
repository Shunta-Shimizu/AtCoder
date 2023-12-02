n = int(input())
H = list(map(int, input().split()))

ans = 0
for h in H:
    if ans < h:
        ans = h
    elif ans >= h:
        break

print(ans)