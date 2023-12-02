n = int(input())
A = list(map(int, input().split()))
q = int(input())

ans = []
for _ in range(q):
    Query = tuple(map(int, input().split()))
    if Query[0] == 1:
        A[Query[1]-1] = Query[2]
    else:
        ans.append(A[Query[1]-1])

print(*ans, sep="\n")