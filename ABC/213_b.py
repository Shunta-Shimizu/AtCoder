n = int(input())
A = list(map(int, input().split()))

A_sort = sorted(A)

ans = A.index(A_sort[-2]) + 1
print(ans)