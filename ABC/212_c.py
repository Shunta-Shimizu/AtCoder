n, m = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

A = sorted(list(A))
B = sorted(list(B))

ans = 10**9+1
i = 0
j = 0
while i < len(A) and j < len(B):
    ans = min(abs(A[i]-B[j]), ans)
    if A[i] > B[j]:
        j += 1
    else:
        i += 1

print(ans)
