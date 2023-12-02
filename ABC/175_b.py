n = int(input())
L = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if len({L[i], L[j], L[k]}) != 3:
                   continue
            l_max = max(L[i], L[j], L[k])
            if l_max ==  L[i]:
                l_res = L[j] + L[k]
            elif l_max == L[j]:
                l_res = L[i] + L[k]
            else:
                l_res = L[i] + L[j]
            
            if l_res > l_max:
                ans += 1

print(ans)
