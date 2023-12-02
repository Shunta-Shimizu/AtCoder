n, d, p = map(int, input().split())
F = list(map(int, input().split()))

F.sort(reverse=True)
ans = sum(F)
tf = False
count = 0
total = sum(F)
for i in range(n):
    if i % d == 0:
        ans = min(ans, total)
        total += p
    
    total -= F[i]

pass_n = 0
if n % d == 0:
    pass_n = n //d
else:
    pass_n = n // d + 1
ans = min(ans, pass_n*p)
print(ans)