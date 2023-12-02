S = input()

abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

if len(S[1:-1]) != 6:
    print("No")
    exit()

if S[0] in abc and S[-1] in abc:
    if S[1] != "0" and S[1] in num[1:] and len(S[1:-1]) == 6:
        for s in S[2:-1]:
            if s not in num:
                print("No")
                exit()
    else:
        print("No")
        exit()
else:
    print("No")
    exit()

print("Yes")
