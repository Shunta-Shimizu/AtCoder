n = int(input())

S = []
for i in range(n):
    s = int(input())
    S.append(s)

S.sort()
ans = sum(S)
for i in range(n):
    if ans % 10 == 0:
        if (ans - S[i]) % 10 != 0:
            ans -= S[i] 
    else:
        print(ans)
        exit()

print(0)