n = int(input())

ans = ""
for i in range(n+1):
    num = 10**8
    for j in range(1, 10):
        if n % j == 0:
            if i % (n//j) == 0:
                num = min(num, j)
    if num == 10**8:
        ans += "-"
    else:
        ans += str(num)

print(ans)        