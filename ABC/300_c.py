h, w = map(int, input().split())
C = []
for _ in range(h):
    c = input()
    C.append(c)

n = min(h, w)
ans = [0 for _ in range(n+1)]
for i in range(h):
    for j in range(w):
        if C[i][j] == "#":
            tf = True
            count = 0
            a = 1
            while tf:
                if i-a < 0 or i+a >= h or j-a < 0 or j+a >= w:
                    tf = False
                else:
                    if C[i-a][j-a] == "#" and C[i+a][j-a] == "#" and C[i-a][j+a] == "#" and C[i+a][j+a] =="#":
                        a += 1
                        count += 1
                    else:
                        tf = False
            ans[count] += 1

print(*ans[1:], sep=" ")
