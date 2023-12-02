n = int(input())
A = set(map(int, input().split()))

A_s = list(A)
A_s.sort()
print(A_s[-2])