n = int(input())

ans = []
for i in range(1 << n):
    s = ""
    count = 0
    for j in range(n):
        if 1 & (i >> j):
            s += "("
            count += 1
        else:
            s += ")"
            count -= 1
        if count < 0:
            break
    if count == 0:
        ans.append(s)

ans.sort()
for a in ans:
    print(a)