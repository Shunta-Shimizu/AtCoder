from collections import defaultdict
S = input()

count = []
for i, si in enumerate(S):
    if i == 0:
        count.append([si, 1])
    else:
        if si == count[-1][0]:
            count[-1][1] += 1
        else:
            count.append([si, 1])

if len(count) == 3 and count[0][0] == "A" and count[1][0] == "B" and count[2][0] == "C":
    print("Yes")
elif len(count) == 1 and count[0][0] == "B":
    print("Yes")
elif len(count) == 1 and count[0][0] == "A":
    print("Yes")
elif len(count) == 1 and count[0][0] == "C":
    print("Yes")
elif len(count) == 2 and count[0][0] == "A" and count[1][0] == "B":
    print("Yes")
elif len(count) == 2 and count[0][0] == "A" and count[1][0] == "C":
    print("Yes")
elif len(count) == 2 and count[0][0] == "B" and count[1][0] == "C":
    print("Yes")
else:
    print("No") 