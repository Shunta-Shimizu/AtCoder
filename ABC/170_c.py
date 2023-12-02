x, n = map(int, input().split())
P = list(map(int, input().split()))

if n == 0:
    print(x)
    exit()

P.sort()
p_min = min(P)
p_max = max(P)
P_set = set(P)
ans = [abs(p_min-1-x)]
i = p_min
while i <= p_max:
    if i not in P_set:
        ans.append(abs(i-x))
    i += 1
ans.append(abs(p_max+1)-x)

ans_i = min(ans)
if x-ans_i not in P_set:
    print(x-ans_i)
else:
    print(x+ans_i)