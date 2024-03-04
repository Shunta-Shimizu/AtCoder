n = int(input())
S = input()

count = [[0 for _ in range(n)] for _ in range(2)]
for i, s in enumerate(S):
    if i == 0:
        if s == "W":
            count[0][i] += 1
        else:
            count[1][i] += 1
    else:
        if s == "W":
            count[0][i] = count[0][i-1]+1
            count[1][i] = count[1][i-1]
        else:
            count[0][i] = count[0][i-1]
            count[1][i] = count[1][i-1]+1

ans = [0 for _ in range(n)]
for i in range(n):
    if S[i] == "W":
        ans[i] += count[0][i]-1
        ans[i] += count[1][-1]-count[1][i]
    else:
        ans[i] += count[0][i]
        ans[i] += count[1][-1]-count[1][i]

# print(count)
print(min(ans))