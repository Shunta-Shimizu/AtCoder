n = int(input())
S = list(input())

if S[0] == "M":
    for i in range(n):
        if i % 2 == 0:
            if S[i] == "M":
                continue
            else:
                print("No")
                exit()
        else:
            if S[i] == "F":
                continue
            else:
                print("No")
                exit()

elif S[0] == "F":
    for i in range(n):
        if i % 2 == 0:
            if S[i] == "F":
                continue
            else:
                print("No")
                exit()
        else:
            if S[i] == "M":
                continue
            else:
                print("No")
                exit()

print("Yes")