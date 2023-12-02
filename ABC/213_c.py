from collections import defaultdict
h, w, n = map(int, input().split())

A = []
B = []
AB = defaultdict(list)
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

A_set = sorted(set(A))
B_set = sorted(set(B))
X = {v: i+1 for i, v in enumerate(A_set)}
Y = {v: i+1 for i, v in enumerate(B_set)}
# print(X)
# print(Y)
for i in range(n):
    print(X[A[i]], Y[B[i]])