s, t, x = map(int, input().split())

if s > t:
    if 0 <= x < t:
        t += 24
        x += 24
    else:
        t += 24
    if x >= s and x < t:
        print("Yes")
    else:
        print("No")
else:
    if s <= x < t:
        print("Yes")
    else:
        print("No")