S = list(input())
n = len(S)
ans = 0

for bit in range(1 << (n-1)):
    s = S[0]
    for i in range(n-1):
        if 1 & (bit >> i): # if (bit & (1 << i)) > 0:
            s += "+"
        s += S[i+1]
        # print(s)
    # print(map(int, s.split("+")))
    ans += sum(map(int, s.split("+")))

print(ans)
            

