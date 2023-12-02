n, m, h, k = map(int, input().split())
S = input()
XY = set()
for _ in range(m):
    x, y = map(int, input().split())
    XY.add((x, y))

now = [0, 0]
for i in range(n):
    if S[i] == "R":
        now[0] += 1
    elif S[i] == "L":
        now[0] -= 1
    elif S[i] == "U":
        now[1] += 1
    elif S[i] == "D":
        now[1] -= 1

    h -= 1
    if h < 0:
        print("No")
        exit()
    else:
       if tuple(now) in XY:
           if h < k:
               XY.discard(tuple(now))
               h = k

print("Yes")

