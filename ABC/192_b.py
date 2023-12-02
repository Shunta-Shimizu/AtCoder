S = list(input())

diff_s = True
for i in range(1, len(S)+1):
    if i % 2 != 0:
        if S[i-1].islower():
            continue
        else:
            diff_s = False
            break
    else:
        if S[i-1].isupper():
            continue
        else:
            diff_s = False
            break
if diff_s:
    print("Yes")
else:
    print("No")