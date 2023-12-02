n = int(input())
S = list(input())
q = int(input())

count = 0
for i in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        if count % 2 == 1:
            if a <= n and b >= n:
                a += n
                b -= n
            elif a < n and b < n:
                a += n
                b += n
            elif a > n and b > n:
                a -= n
                b -= n
    
        tmp = S[a-1]
        S[a-1] = S[b-1]
        S[b-1] = tmp    
    else:
        count += 1

if count % 2 == 1:
    front = S[:n]
    back = S[n:]
    S = back + front

print(*S, sep="")