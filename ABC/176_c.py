n = int(input())
A = list(map(int, input().split()))

ans = []
for i in range(1, n):
    if A[i-1] > A[i]:
        ans.append(A[i-1]-A[i])
        A[i] += A[i-1]-A[i]

print(sum(ans))