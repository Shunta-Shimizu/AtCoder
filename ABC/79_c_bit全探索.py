S = input()
n = len(S) 
for bit in range(1 << n):
    ans = int(S[0])
    s = S[0]
    for i in range(n-1):
        if 1  & (bit >> i):
            ans += int(S[i+1])
            s += "+"
        else:
            ans -= int(S[i+1])
            s += "-"
        s += S[i+1]
    
    if ans == 7:
        s += "=7"
        print(s)
        break
    
