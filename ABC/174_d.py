n = int(input())
C = list(input())

nr = 0
nw = 0
for i, c in enumerate(C):
    if c == "R":
        nr += 1
    else:
        nw += 1

dr = 0
dw = 0
for i, c in enumerate(C):
    if i < nr:
        if c == "W":
            dw += 1
    else:
        if c == "R":
            dr += 1

if dr >= dw:
    ans = dr+dr-dw
else:
    ans = dw+dw-dr

print(ans)