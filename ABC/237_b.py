h, w = map(int, input().split())

A = []
for _ in range(h):
    A.append(list(map(int, input().split())))

B = []
for i in range(w):
    B.append([])
    for j in range(h):
        B[i].append(A[j][i])
    
    print(*B[i])

# B = list(zip(*A))
# for b in B:
#     print(*b)