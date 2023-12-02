n = int(input())
A = list(map(int, input().split()))

ans = 0
k_max = 0
for i in range(2, max(A)+1):
    k = 0
    for a in A:
        if a % i == 0:
            k += 1
    if k > k_max:
        ans = i
        k_max = k

print(ans)