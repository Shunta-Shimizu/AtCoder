n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for i in range(n):
    if B[i] < A[i]:
        ans += B[i]
    else:
        ans += A[i]
        if (B[i]-A[i]) < A[i+1]:
            ans += (B[i]-A[i])
            A[i+1] -= (B[i]-A[i])
        else:
            ans += A[i+1]
            A[i+1] = 0
    
print(ans)
