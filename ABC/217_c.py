n = int(input())
P = list(map(int, input().split()))

Q = [0 for _ in range(n)]
for i in range(n):
    Q[P[i]-1] = i+1
    
print(*Q, sep=" ")