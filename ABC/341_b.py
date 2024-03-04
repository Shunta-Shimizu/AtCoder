n = int(input())
A = list(map(int, input().split()))
S = []
T = []
for _ in range(n-1):
    s, t = map(int, input().split())
    S.append(s)
    T.append(t)

for i in range(n-1):
    if A[i] >= S[i]:
        b = (A[i]//S[i])
        ta = T[i]*b
        A[i+1] += ta

print(A[n-1])
    