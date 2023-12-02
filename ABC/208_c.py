n, k = map(int, input().split())
A = list(map(int, input().split()))

Info = []
for i in range(n):
    Info.append([i, A[i], 0])

Info = sorted(Info, key=lambda x:x[1])

for i in range(n):
    Info[i][2] += k//n

res = k-(n*(k//n))
i = 0
while res > 0:
    Info[i%n][2] += 1
    i += 1
    res -= 1

Info = sorted(Info, key=lambda x:x[0])
for _, _, ans in Info:
    print(ans)

