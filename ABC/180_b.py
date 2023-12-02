import math

n = int(input())
X = list(map(int, input().split()))

manhattan = 0
euclid = 0
chebyshev = 0
for i in range(n):
    manhattan += abs(X[i])
    euclid += abs(X[i]) ** 2
    chebyshev = max(chebyshev, abs(X[i]))

print(manhattan)
print(math.sqrt(euclid))
print(chebyshev)