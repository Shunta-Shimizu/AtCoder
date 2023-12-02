# n = int(input())
# S = list(input())

# tf_a = False
# tf_b = True
# for i in range(n):
#     if S[i] == "o":
#         tf_a = True
#     elif S[i] == "x":
#         tf_b = False

# if tf_a == True and tf_b == True:
#     print("Yes")
# else:
#     print("No")

n = int(input())
A = []
a_count = 0
for _ in range(n):
    a = list(map(int, input().split()))
    a_count = a.count(1)
    A.append(a)

B = []
b_count = 0
for _ in range(n):
    b = list(map(int, input().split()))
    b_count += b.count(1)
    B.append(b)

ans = 0
for i in range(n):
    for j in range(n):
        if A[i][j] == 1:
            if A[i][j] == B[i][j]:
                continue
            else:
                for k in range(n):
                    for l in range(n):
                        A[k][l] = A[n-l-1][k]

print(A)