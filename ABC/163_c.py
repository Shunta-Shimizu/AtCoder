n = int(input())
A = list(map(int, input().split()))

ans = [0 for _ in range(n)]
for i in range(n-1):
    ans[A[i]-1] += 1

for i in range(n):
    print(ans[i])