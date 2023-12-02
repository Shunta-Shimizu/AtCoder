n, k, m = map(int, input().split())
A = list(map(int, input().split()))

total = sum(A)

for i in range(k+1):
    if (total + i) / n >= m:
        print(i)
        exit()

print(-1)