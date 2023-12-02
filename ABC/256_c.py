h1, h2, h3, w1, w2, w3 = map(int, input().split())

ans = 0
for a11 in range(1, 29):
    for a12 in range(1, 29):
        a13 = h1 - a11 - a12
        if a13 <= 0:
            continue
        else:
            if a11 + a12 + a13 == h1:
                for a21 in range(1, 29):
                    for a22 in range(1, 29):
                        a23 = h2 - a21 - a22 
                        if a23 <= 0:
                            continue
                        else:
                            if a21 + a22 + a23 == h2:
                                a31 = w1 - a11 - a21
                                a32 = w2 - a12 - a22
                                a33 = w3 - a13 - a23
                                if a31 <= 0 or a32 <= 0 or a33 <= 0:
                                    continue
                                else:
                                    if a31 + a32 + a33 == h3:
                                        ans += 1

print(ans)
