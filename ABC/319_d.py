from collections import defaultdict
n = int(input())

count = [0 for _ in range(5)]
for _ in range(n):
    s = input()
    if s[0] == "M":
        count[0] += 1
    elif s[0] == "A":
        count[1] += 1
    elif s[0] == "R":
        count[2] += 1
    elif s[0] == "C":
        count[3] += 1
    elif s[0] == "H":
        count[4] += 1

ans = 0
for i in range(1<<5):
    if bin(i)[2:].count("1") == 3:
        c = 0
        tf = False
        for j in range(5):
            if 1 & (i>>j) == 1:
                if not tf:
                    c += count[j]
                    tf = True
                else:
                    c *= count[j]
        ans += c
     
print(ans)