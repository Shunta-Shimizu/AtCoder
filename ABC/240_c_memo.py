# メモ化再帰
from collections import defaultdict
def f(i, x):
    if i == n:
        return x == X
    arg = (i, x)
    if arg in memo:
        return memo[arg]
    res = False
    if f(i + 1, x + A[i]) or f(i + 1, x + B[i]):
        res = True
    memo[arg] = res
    return res

n, X = map(int, input().split())
A = []
B = []
for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

memo = defaultdict(bool)
if f(0, 0):
    print("Yes")
else:
    print("No")