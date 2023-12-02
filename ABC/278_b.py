H, M = map(int, input().split())

a = H // 10
b = H % 10
c = M // 10
d = M % 10

if b >= 6:
    b += 1
    c = 0
    d = 0
    H = 10*a + b
    M = 10*c + d
elif c >= 4:
    if a <= 1:
        H = 10*a + b
        M = 10*c + d
    else:
        b += 1
        c = 0
        d = 0
        H = 10*a + b
        M = 10*c + d

if H // 10 == 2 and H % 10 >= 4:
    H = 0
elif H // 10 == 1 and H % 10 >= 6:
    H = 20

print(H, M, sep=" ")