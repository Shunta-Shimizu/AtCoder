x, y, z = map(int, input().split())
S = input()

count = [[S[0], 1]]
for i in range(1, len(S)):
    if S[i] == count[-1][0]:
        count[-1][1] += 1
    else:
        count.append([S[i], 1])
 
ans = 0
caps = False
for s, c in count:
    if s == "A":
        if caps:
            ans += x*c
        else:
            if z+x*c <= y*c:
                ans += z+x*c
                caps = True
            else:
                ans += y*c
    else:
        if caps:
            if z+x*c <= y*c:
                caps = False
                ans += z+x*c
            else:
                ans += y*c
        else:
            ans += x*c
          
print(ans)
