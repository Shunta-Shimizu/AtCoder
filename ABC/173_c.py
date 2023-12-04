h, w, k = map(int, input().split())

C_copy = []
count = 0
for _ in range(h):
    c = list(input())
    count += c.count("#")
    C_copy.append(c)

ans = 0
for bit_h in range(1 << h):
    C = C_copy.copy()
    for i in range(h):
        if 1 & (bit_h >> i):
            C[i] = ["." for _ in range(w)]
    # print(C)
    C2 = list(zip(*C))
    for bit_w in range(1 << w):
        Ct = C2.copy()
        for j in range(w):
            if 1 & (bit_w >> j):
                Ct[j] = ["." for _ in range(h)]
    
        # print(Ct)
        cnt = 0
        for ct in Ct:
            cnt += list(ct).count("#")
        
        if cnt == k:
            ans += 1

print(ans)