n = input()

ans = 0
for num in range(1 << len(n)):
    n_1 = ""
    n_2 = ""
    for i in range(len(n)):
        if 1 & (num >> i) == 1:
            n_1 += n[i]
        else:
            n_2 += n[i]

    if len(n_1) == 0 or len(n_2) == 0:
        continue
    else:
        n_1 = sorted(list(n_1), reverse=True)
        a = ""
        for n1 in n_1:
            a += n1
        n_2 = sorted(list(n_2), reverse=True)
        b = ""
        for n2 in n_2:
            b += n2

        ans = max(ans, int(a)*int(b))

print(ans)