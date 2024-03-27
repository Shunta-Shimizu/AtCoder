n = int(input())
A = list(map(int, input().split()))

ans = []
for i, a in enumerate(A):
    if i == n-1:
        break
    else:
        ans.append(A[i]*A[i+1])

print(*ans)