n = int(input())
S = list(input())

ans = 0
for i in range(1, n-1):
    S_first = set(S[:i])
    S_second = set(S[i:])
    count = 0
    for sf in S_first:
        if sf in S_second:
            count += 1
    ans = max(ans, count)

print(ans)
            

