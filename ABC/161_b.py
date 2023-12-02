n, m = map(int, input().split())
A = list(map(int, input().split()))

a_sum = sum(A)
count = 0
for i in range(n):
    if A[i] < a_sum * (1 / (4 * m)):
        continue
    else:
        count += 1

if count >= m:
    print("Yes")
else:
    print("No")