n = int(input())
S = []
for _ in range(n):
    s = list(input())
    S.append(s)

tf = False
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        else:
            ans = S[i] + S[j]
            count = 0
            for k in range(len(ans)//2):
                if ans[k] == ans[-(k+1)]:
                    count += 1
            
            if count == len(ans) // 2:
                print("Yes")
                exit()
print("No")

