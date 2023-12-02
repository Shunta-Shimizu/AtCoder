n, x = map(int, input().split())
A = list(map(int, input().split()))


for i in range(101):
    A.append(i)
    A.sort()
    sum_a = sum(A[1:n-1])
    if sum_a >= x:
        print(i)
        exit()
    A.remove(i)
    
print(-1)