n = int(input())
A = list(map(int, input().split()))

s = 0
l = 7
for i in range(n):
    print(sum(A[s:l]), end=" ")
    s += 7
    l += 7