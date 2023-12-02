n = int(input())
X = list(map(int, input().split()))

X.sort()
for i in range(n):
    X.pop(0)
    X.pop(-1)

ans = sum(X) / len(X)
print(ans)