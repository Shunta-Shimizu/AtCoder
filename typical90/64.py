from collections import defaultdict
n, q = map(int, input().split())
A = list(map(int, input().split()))
diff = defaultdict(int)
ans = 0
for i in range(n-1):
    diff[(i, i+1)] = A[i+1]-A[i]
    ans += abs(A[i+1]-A[i])

for _ in range(q):
    l, r, v = map(int, input().split())
    l -= 1
    r -= 1
    f = 0
    if l > 0:
        f += abs(diff[(l-1, l)])
        diff[(l-1, l)] += v
    if r < n-1:
        f += abs(diff[(r, r+1)])
        diff[(r, r+1)] -= v
    
    b = abs(diff[(l-1, l)]) + abs(diff[(r, r+1)])
    ans += b-f
    print(ans)