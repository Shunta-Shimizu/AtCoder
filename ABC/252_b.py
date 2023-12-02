n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a_max = max(A)
a_max_idx = []
for i in range(n):
    if A[i] == a_max:
        a_max_idx.append(i+1)

for a_idx in a_max_idx:
    if a_idx in B:
        print("Yes")
        exit()

print("No")
