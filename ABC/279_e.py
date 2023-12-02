n, m = map(int, input().split())
A = list(map(int, input().split()))
B = [i for i in range(1, n+1)]
K = [j for j in range(1, m+1)]

for i in range(1, m+1):
    # B = [i for i in range(1, n+1)]
    for k in K:
        if k == i:
            continue
        else:
            temp = B[A[k-1]-1]
            B[A[k-1]-1] = B[A[k-1]]
            B[A[k-1]] = temp

    print(B.index(1)+1)

