n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


A_pair = []
B_pair = []
for i in range(n):
    A_pair.append(["A", A[i]])

for j in range(m):
    B_pair.append(["B", B[j]])

C = A_pair + B_pair
C.sort(key=lambda x:x[1])

ans_A = []
ans_B = []
for i in range(n+m):
    if C[i][0] == "A":
        ans_A.append(i+1)
    else:
        ans_B.append(i+1)

print(*ans_A, sep=" ")
print(*ans_B, sep=" ")