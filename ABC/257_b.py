n, k, q = map(int, input().split())

grid = list(i+1 for i in range(n))
A = list(map(int, input().split()))
L = list(map(int, input().split()))

for l in L:
    if A[l-1] == grid[n-1]:
        continue
    elif A[l-1] + 1 in A:
        continue
    else: 
        A[l-1] += 1

print(*A, sep=" ")
