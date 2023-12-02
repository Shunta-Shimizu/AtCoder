import functools
import math

n = int(input())
A = list(map(int, input().split()))

A_gcd = functools.reduce(math.gcd, A)

A = [a//A_gcd for a in A]

i = 0
div_count = 0
while i < len(A):
    if A[i] % 2 == 0:
        A[i] = A[i] // 2
        div_count += 1
    elif A[i] % 3 == 0:
        A[i] = A[i] // 3
        div_count += 1
    else:
        if A[i] != 1:
            print(-1)
            exit()
        else:
            i += 1

print(div_count)




