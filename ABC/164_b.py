a, b, c, d = map(int, input().split())

i = 0
while True:
    if i % 2 == 0:
        c -= b
    else:
        a -= d
    if c <= 0 or a <= 0:
        break
    i += 1

if i % 2 == 0:
    print("Yes")
else:
    print("No")