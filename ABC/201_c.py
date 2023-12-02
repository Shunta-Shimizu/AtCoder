import itertools
from collections import defaultdict
S = list(input())

oq = defaultdict(list)
for i in range(len(S)):
    if S[i] == "o":
        oq["o"].append(str(i))
    elif S[i] == "?":
        oq["q"].append(str(i))

# if len(oq["o"]) > 4:
#     print(0)
#     exit()

A = []
for i in range(10):
    A.append(str(i))

nums = list(itertools.product(A, repeat=4))
ans = 0
for n in nums:
    count_o = 0
    count_q = 0
    C = defaultdict(bool)
    for i in range(4):
        if n[i] in oq["o"]:
            if C[n[i]]:
                count_q += 1
            else:
                count_o += 1
                C[n[i]] = True
        elif n[i] in oq["q"]:
            count_q+= 1
    
    if count_o == len(oq["o"]) and count_o+count_q == 4:
        ans += 1

print(ans)
