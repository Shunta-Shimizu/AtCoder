S = input()

s = ""
ans = 0
for i in range(len(S)):
    if S[i] == "A" or S[i] == "C" or S[i] == "G" or S[i] == "T":
        s += S[i]
    else:
        s = ""
    ans = max(ans, len(s))
    
print(ans)