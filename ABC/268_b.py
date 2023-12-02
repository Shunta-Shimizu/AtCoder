S = input()
T = input()

S = list(S)
T = list(T)

if len(S) > len(T):
    print("No")
    exit()

count = 0
for i in range(len(S)):
    if S[i] == T[i]:
        count += 1

if count == len(S):
    print("Yes")
else:
    print("No")


