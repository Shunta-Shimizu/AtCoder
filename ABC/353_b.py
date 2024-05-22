n, k = map(int, input().split())
A = list(map(int, input().split()))

i = 0
ans = 0
tmp = 0
while i < n:
    if tmp+A[i] > k:
        ans += 1
        tmp = A[i]
        i += 1
    else:
        tmp += A[i]
        i += 1

print(ans+1)