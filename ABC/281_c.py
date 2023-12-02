n, t = map(int, input().split())
A = list(map(int, input().split()))

roop = t // sum(A)
rest = t % sum(A)
# print(roop)
# print(rest)
for i in range(n):
    if rest // A[i] == 0:
        print(i+1, rest % A[i])
        break
    else:
        rest = rest - A[i]

