n, x = map(int, input().split())
A = list(map(int, input().split()))

for i in range(n):
    if A[i] == x:
        A[i] = ""

print(*A, sep=" ")

