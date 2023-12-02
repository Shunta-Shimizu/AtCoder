n , k = map(int, input().split())

A = []
for _ in range(k):
    d = int(input())
    A.append(list(map(int, input().split())))

tf = [False for _ in range(n)] 
for i in range(k):
    for a in A[i]:
        tf[a-1] = True

ans = 0
for x in tf:
    if not x:
        ans += 1

print(ans)
