A, B = map(str, input().split())

A = list(reversed(A))
B = list(reversed(B))

n = len(A)
m = len(B)

if n >= m:
    num = m
else:
    num = n

for i in range(num):
    if int(A[i]) + int(B[i]) >= 10:
        print("Hard")
        exit()

print("Easy")
