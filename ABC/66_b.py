S = list(input())

S_first = S[:len(S)//2]
S_second = S[len(S)//2:]
while True:
    S_second = S_second[:-1]
    if S_first == S_second:
        ans = S_first + S_second
        print(len(ans))
        break
    else:
        S = S_first + S_second
        S_first = S[:len(S)//2]
        S_second = S[len(S)//2:]