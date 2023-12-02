n = int(input())
A = []
for _ in range(n):
    a = int(input())
    A.append(a)

A_sort = sorted(A, reverse=True)
a_max = max(A)
for i in range(n):
    if A[i] == a_max:
        print(A_sort[1])
    else:
        print(a_max)