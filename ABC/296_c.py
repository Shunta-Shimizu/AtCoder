n, x = map(int, input().split())
A = list(map(int, input().split()))

A_set = set(A)
for i in range(n):
    if A[i] - x in A_set:
        print("Yes")
        exit()

print("No")
