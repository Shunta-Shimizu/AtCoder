A = []
while True:
  a = int(input())
  A.append(a)
  if a == 0:
    break

a1 = A[0]
A = sorted(A[1:])

A.append(a1)
print(*A, sep="\n")