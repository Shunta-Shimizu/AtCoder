n = int(input())
D = list(map(int, input().split()))

D.sort()
m1 = D[n//2-1]
m2 = D[n//2]

print(m2-m1)