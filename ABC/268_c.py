n = int(input())
P = list(map(int, input().split()))

count = [0] * n

for i in range(n):
    p = P[i]
    x0 = (p-i-1) % n
    x1 = (p-i) % n
    x2 = (p-i+1) % n
    count[x0] += 1
    count[x1] += 1
    count[x2] += 1
    print(count)
    
print(max(count))