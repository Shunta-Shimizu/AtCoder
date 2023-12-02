n, a, b = map(int, input().split())
S = input()
S_true = S
cost = 0
cost_list = []

for i in range(n):
    cost = a * i
    S_f = S[:i]
    S = S[i:] + S_f
    # print(S)
    for j in range(n//2):
        if S[j] != S[-(j+1)]:
            cost += b
            # print(S[j], S[-(j+1)])
    cost_list.append(cost)
    S = S_true

# print(cost_list)
print(min(cost_list))
