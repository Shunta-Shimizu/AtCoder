import math
n, x = map(int, input().split())
A = list(map(int, input().split()))

A.append(x)
A.sort()
A_diff = []

if len(A) == 2:
    print(A[1]-A[0])
elif  len(A) == 3:
    print(math.gcd(A[1]-A[0], A[2]-A[1]))
else:
    for i in range(n-1):
        diff = A[i+1]-A[i]
        A_diff.append(diff)
        
    A_diff.sort(reverse=True)
    ans = math.gcd(A_diff[0], A_diff[1])
    for i in range(2, len(A_diff)):
        ans = math.gcd(ans, A_diff[i])

    print(ans)
