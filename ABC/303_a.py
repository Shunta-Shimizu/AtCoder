n = int(input())
S = input()
T = input()
tf = True
for i in range(n):
    if S[i] == T[i]:
        continue
    elif (S[i] == "l" and T[i] == "1") or (S[i] == "1" and T[i] == "l"):
        continue
    elif (S[i] == "o" and T[i] == "0") or (S[i] == "0" and T[i] == "o"):
        continue
    else:
        tf = False

if not tf:
    print("No")
else:
    print("Yes")

    