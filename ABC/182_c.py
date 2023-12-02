n = input()

ans = {0}
for num in range(1, 1 << len(n)):
    n_list = list(n)
    for i in range(len(n)):
        if 1 & (num >> i) == 1:
            continue
        else:
            n_list[i] = 0
    m = "0"
    for i in range(len(n_list)):
        if n_list[i] == 0:
            continue
        else:
            m += n_list[i]
    m = int(m)
    if m % 3 == 0:
        ans.add(m)
    
if max(ans) == 0:
    print(-1)
else:
    print(len(n)-len(str(max(ans))))