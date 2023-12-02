n, k = map(int, input().split())
A = set(map(int, input().split()))

ans = 0
for i in range (k):
    if i in A:
        ans = i + 1
    else:
        break

print(ans)
    
