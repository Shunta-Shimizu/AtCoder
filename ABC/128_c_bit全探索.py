n, m = map(int, input().split())

k_list = []
S_list = []
for _ in range(m):
    kS = list(map(int, input().split()))
    k = kS[0]
    S = kS[1:]
    k_list.append(k)
    S_list.append(S)

P = list(map(int, input().split()))

ans = 0
tf = False
for i in range(m):
    count = 0
    for bit in range(k_list[i]):
        for i in range(len(S_list[i])):
            if 1 & (bit >> i):
                count += 1
        if count % 2 == P[i]:
            tf = True
        else:
            tf = False
            break
    if tf:
        ans += 1

print(ans)
