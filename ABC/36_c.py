n = int(input())
A = []
for _ in range(n):
    A.append(int(input()))

A_set = sorted(set(A))
ans = {v:i for i, v in enumerate(A_set)}

for i in range(n):
    print(ans[A[i]])