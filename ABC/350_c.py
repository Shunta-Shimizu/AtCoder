n = int(input())
A = list(map(int, input().split()))

ans = []
for i in range(n):
    while i+1 != A[i]:
        ans.append((i + 1, A[i]))
        tmp = A[i]
        A[i] = A[A[i]-1]
        A[A[i]-1] = tmp

print(len(ans))
for a in ans:
    print(*a)
