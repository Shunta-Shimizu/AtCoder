S = list(input())
T = list(input())

n = len(S)

if S == T:
    print("Yes")
    exit()

for i in range(n-1):
    tmp = S[i]
    S[i] = S[i+1]
    S[i+1] = tmp

    if S == T:
        print("Yes")
        exit()
    else:
        tmp = S[i]
        S[i] = S[i+1]
        S[i+1] = tmp

print("No")