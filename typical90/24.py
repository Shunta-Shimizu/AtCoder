n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

count = 0
for i in range(n):
    count += abs(A[i]-B[i])

if k < count:
    print("No")
else:
    if (k-count) % 2 == 0:
        print("Yes")
    else:
        print("No")