n = int(input())
A = list(map(int, input().split()))

A.sort()

for i in range(n):
    if i+1 != A[i]:
        print("No")
        exit()

print("Yes")