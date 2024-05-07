from collections import defaultdict
S = input()
T = input()

now = 0
ans = ""
for t in T:
    if now >= len(S):
        break
    for i in range(now, len(S)):
        if t.lower() == S[i]:
            ans += t
            now = i+1
            break

if len(ans) == 2:
    if ans+"X" == T:
        print("Yes")
    else:
        print("No")
elif len(ans) == 3:
    if ans == T:
        print("Yes")
    else:
        print("No")
else:
    print("No")