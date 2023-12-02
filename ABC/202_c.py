from collections import defaultdict

n =int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

B_c = defaultdict(int)

for i in range(n):
    B_c[B[C[i]-1]] += 1

# print(B_c)
ans = 0
for i in range(n):
    if A[i] in B_c:
        ans += B_c[A[i]]

print(ans)