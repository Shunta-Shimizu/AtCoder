n, m = map(int,input().split())
S = input()

ans = 10**8
for i in range(1001):
    mnow = m
    logo = i
    tf = True
    for j, s in enumerate(S):
        if s == "0":
            mnow = m
            logo = i
        elif s == "1":
            if mnow <= 0 and logo <= 0:
                tf= False
                break
            else:
                if mnow > 0:
                    mnow -= 1
                else:
                    logo -= 1
        else:
            if logo <= 0:
                tf = False
                break
            else:
                logo -= 1
    
    if tf:
        ans = min(ans, i)

print(ans)