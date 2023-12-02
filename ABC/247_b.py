from collections import defaultdict
n = int(input())

S = []
T = []
tf = defaultdict()
for i in range(n):
    s, t = map(str, input().split())
    S.append(s)
    T.append(t)
    tf[i] = [True, True]


for i in range(n):
    for num in range(2):
        if num == 0:
            a = S[i]
        else:
            a = T[i]
        for j in range(n):
            if i != j:
                if a == S[j] or a == T[j]:
                    tf[i][num] = False
    if not tf[i][0] and not tf[i][1]:
        print("No")
        exit()

print("Yes")

# n = int(input())

# S = []
# T = []
# for _ in range(n):
#     s, t = map(str, input().split())
#     S.append(s)
#     T.append(t)

# for i in range(n):
#     S_tf = False
#     T_tf = False
#     for j in range(n):
#       if i != j:
#           if S[i] == S[j] or S[i] == T[j]:
#               S_tf = True
#           if T[i] == S[j] or T[i] == T[j]:
#               T_tf = True
#           if S_tf and T_tf:
#               print("No")
#               exit()
            
# print("Yes")