n = int(input())
A = []
for _ in range(n):
    a = list(map(int, input().split()))
    A.append(a)

for a in A:
    ans = []
    for i, b in enumerate(a):
        if b == 1:
            ans.append(i+1)
    
    print(*ans)
