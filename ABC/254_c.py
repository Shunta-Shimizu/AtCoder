n, k = map(int, input().split())
A = list(map(int, input().split()))
A_sort = sorted(A)

for i in range(k):
    A_slice = []
    for j in range(i, n, k): 
        A_slice.append(A[j])
    A_slice.sort()
    # print(A_slice)
    for l in range(i, n, k):
        A[l] = A_slice[l//k]

# print(A)
if A == A_sort:
    print("Yes")
else:
    print("No")