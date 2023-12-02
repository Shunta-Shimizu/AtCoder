n, q = map(int, input().split())

L = []
A = []
for _ in range(n):
    LA = list(map(int, input().split()))
    A.append(LA[1:])

ans = []
for _ in range(q):
    s, t = map(int, input().split())
    ans.append(A[s-1][t-1])

print(*ans, sep="\n")