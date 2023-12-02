n, k = map(int, input().split())
A = list(map(int, input().split()))

for _ in range(k):
    A.pop(0)
    A.append(0)

for i in A:
    print(i, end=" ")