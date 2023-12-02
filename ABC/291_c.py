from collections import defaultdict

n = int(input())
S = input()

x = 0
y = 0
tf = False
# passed = defaultdict(set)
# passed[0].add(0)
passed = {(x, y)}
for i in range(n):
    if S[i] == "R":
        x += 1
        y += 0
    elif S[i] == "L":
        x -= 1
        y += 0
 
    elif S[i] == "U":
        x += 0
        y += 1
 
    elif S[i] == "D":
        x += 0
        y -= 1
    # if y in passed[x]:
    if (x, y) in passed:
        tf = True
        break
    else:
        # passed[x].add(y)
        passed.add((x, y))

if tf:
    print("Yes")
else:
    print("No")


