n = int(input())

ans = 0
for a in range(1, n+1):
    # if n - a*b >= 1:
    #  b = (n-1) // a
    ans += (n-1) // a

print(ans)

