n, m = map(int, input().split())

S = []
C = []
for _ in range(m):
    s, c = map(int, input().split())
    S.append(s)
    C.append(c)

if n > 1 and m == 0:
    print(10**(n-1))
elif n == 1 and m == 0:
    print(0)
else:
    if n == 1:
        num = 0
    else:
        num = 10**(n-1)
    for i in range(num, 10**n):
        for j in range(m):
            if str(i)[S[j]-1] == str(C[j]):
                if j == m-1:
                    print(i)
                    exit()
                else:
                    continue
            else:
                break
    
    print(-1)