S = input()
T = input()


for i in range(len(list(S))-len(list(T))+1):
    if S[i:(i+len(list(T)))] == T:
        print("Yes")
        exit()

print("No")    
