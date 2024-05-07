from collections import defaultdict
n = int(input())
P = list(map(int, input().split()))

tf = defaultdict(bool)
for i, p in enumerate(P):
    if p == i+1:
        tf[p] = True
    else:
        tf[p] = False
    
ans = 0
for i in range(n):
    if i == 0:
        if tf[P[i]]:
            tmp = P[i]
            P[i] = P[i+1]
            P[i+1] = tmp
            tf[P[i]] = False
            ans += 1
            if P[i+1] == i+2:
                tf[P[i+1]] = True
            else:
                tf[P[i+1]] = False
    elif i == n-1:
        if tf[P[i]]:
            tmp = P[i]
            P[i] = P[i-1]
            P[i-1] = tmp   
            ans += 1  
    else:
        if tf[P[i]]:
            if tf[P[i+1]]:
                tmp = P[i]
                P[i] = P[i+1]
                P[i+1] = tmp
                tf[P[i]] = False
                tf[P[i+1]] = False
                ans += 1
            else:
                tmp = P[i]
                P[i] = P[i+1]
                P[i+1] = tmp
                tf[P[i]] = False
                tf[P[i+1]] = False
                ans += 1
                if P[i+1] == i+2:
                    tf[P[i+1]] = True
                else:
                    tf[P[i+1]] = False               

print(ans)