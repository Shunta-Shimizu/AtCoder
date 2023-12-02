n = int(input())
A = list(map(int, input().split()))

ans = [0 for _ in range(2*n)]
for i in range(n):
    if i == 0:
        ans[2*i] = 1
        ans[2*i+1] = 1
    else:
        ans[2*i] = ans[A[i]-2] + 1
        ans[2*i+1] = ans[A[i]-2] + 1

for i in range(2*n+1):
    if i == 0:
        print(0)
    else:
        print(ans[i-1])