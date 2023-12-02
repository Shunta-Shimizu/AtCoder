n = int(input())
S = list(input())

l_f = 0
l_l = 0
c = 0
for i in range(n):
    if S[i] == "|" and c == 0:
        l_f = i
        c = 1
    if S[i] == "|" and c == 1:
        l_l = i

S_s = S[l_f:l_l]
if "*" in S_s:
    print("in")
else:
    print("out")