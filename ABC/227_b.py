n = int(input())
S = list(map(int, input().split()))

count = 0
for i in range(n):
    s = S[i]
    tf = False
    for j in range(1, s+1):
        for k in range(1, s+1):
            if 4 * j * k + 3 * j + 3 * k == s:
                tf = True
                break
        if tf:
            count += 1
            break

print(n - count)