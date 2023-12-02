n, k, x = map(int, input().split())
A = list(map(int, input().split()))

A_sum = sum(A)
for i in range(n):
    m = A[i] // x
    if m <= k:
        A_sum -= m * x
        A[i] -= m * x
        k -= m
    
    if k == 0 or A_sum <= 0:
        print(A_sum)
        exit()

A.sort(reverse=True)

for i in range(n):
    if A[i] < x:
        A_sum -= A[i]
    else:
        A_sum -= x
    k -= 1
    if k == 0 or A_sum == 0:
        break

print(A_sum)