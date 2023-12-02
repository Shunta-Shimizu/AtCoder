n = int(input())
A = list(map (int, input().split()))

Ans = []
cut = 0
for i in range(n+1):
    if i == 0:
        Ans.append(0)
        Ans.append(360)
    else:
        cut += A[i-1]
        Ans.append(cut % 360)

Ans.sort()
# print(Ans)

max_d = 0
for i in range(len(Ans)-1):
    if Ans[i+1] - Ans[i] > max_d:
        max_d = Ans[i+1] - Ans[i]

print(max_d) 
