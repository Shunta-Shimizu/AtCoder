n = int(input())
S = input()

at = False
bt = False
ct = False
for i in range(n):
    if S[i] == "A":
        at = True
    elif S[i] == "B":
        bt = True
    elif S[i] == "C":
        ct = True
    
    if at and bt and ct:
        print(i+1)
        exit()

    
