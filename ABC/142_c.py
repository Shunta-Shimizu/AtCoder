n = int(input())
A = list(map(int, input().split()))

ans = [0 for _ in range(n)]
for i in range(n):
    ans[A[i]-1] = i+1

print(*ans, sep=" ")