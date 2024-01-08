n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = 0

for i in range(n):
    if i == 0:
        ans += B[A[i]-1]
    else:
        ans += B[A[i]-1]
        if A[i]-A[i-1] == 1:
            ans += C[A[i-1]-1]

print(ans)
