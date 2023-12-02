S = list(input())

n = len(S)
if S == S[::-1]:
    if S[:(n-1)//2] == S[:(n-1)//2:-1]:
        S_3 = S[(n+3)//2-1:n]
        # if S[(n+3)//2-1:n] == S[(n+3)//2-1:n:-1]:
        if S_3 == S_3[::-1]:
            print("Yes")
        else:
            # print(S[(n+3)//2-1:n], S[(n+3)//2-1:n:-1])
            # print(S[:(n-1)//2], S[:(n-1)//2:-1])
            print("No")
    else:
        print("No")
else:
    print("No")