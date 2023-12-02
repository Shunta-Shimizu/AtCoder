n, x = map(int, input().split())
A = list(map(int, input().split()))

sum = 0
for i in range(n):
    if i % 2 == 0:
        sum += A[i]
    else:
        sum += A[i] - 1

if sum <= x:
    print("Yes")
else:
    print("No")