n = int(input())

Ans = []
for i in range(n):
    if i == 0:
        S = [1]
        Ans.append(S)
    else:
        S = Ans[i-1] + [i+1] + Ans[i-1]
        Ans.append(S)

print(*Ans[-1])