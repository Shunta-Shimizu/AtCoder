h, m = map(int, input().split())

if h <= 15:
    h2 = h
    m2 = m
elif 15< h <20:
    h2 = 20
    m2 = 0
elif h >= 20:
    if m >= 40:
        h2 = h + 1
        m2 = 0
        if h2 >= 24:
            h2 = 0
            m2 = 0
    else:
        h2 = h
        m2 = m

print(h2, m2)
