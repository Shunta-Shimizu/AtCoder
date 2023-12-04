n ,s, m, l = map(int, input().split())

ans = 10**10
for i in range(20):
    for j in range(15):
        for k in range(10):
            if i*6+j*8+k*12 >= n:
                ans = min(ans, s*i+m*j+l*k)

print(ans)