n, a, b = map(int, input().split())
S = input()
# S_true = S
S+=S
cost = 0
ans =1 << 60
for i in range(n):
    cost = a * i
    for j in range(n//2):
        if S[i+j] != S[i+n-1-j]:
            cost += b
    ans = min(ans, cost)
    # S = S_true

print(ans)
