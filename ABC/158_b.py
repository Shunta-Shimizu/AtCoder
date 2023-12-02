n, a, b = map(int, input().split())

i = n // (a + b)
j = n % (a + b)

ans = a * i
if j >= a:
    ans += a
else:
    ans += j

print(ans)