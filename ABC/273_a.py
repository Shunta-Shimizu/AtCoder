N = int(input())

f0 = 1
ans = f0

for i in range(N, 1, -1):
    ans = ans * i

print(ans)