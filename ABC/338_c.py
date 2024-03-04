n = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a_max = [0 for _ in range(n)]
for j, a in enumerate(A):
    if a == 0:
        a_max[j] = Q[j]
    else:
        a_max[j] = Q[j]//a 

a_min = min(a_max)
ans = 0
for ai in range(a_min+1):
    b_max = [0 for _ in range(n)]
    for j, bi in enumerate(B):
        if bi == 0:
            b_max[j] = 10**8
        else:
            b_max[j] = (Q[j]-A[j]*ai) // bi
    
    ans = max(ans, ai+min(b_max))

print(ans)
