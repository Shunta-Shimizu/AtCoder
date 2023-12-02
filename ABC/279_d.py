from math import sqrt

a, b = map(int, input().split())

def f(x):
    return b*x + a/sqrt(x+1)

left = 0
right = a//b

while right - left > 2:
    center1 = (left*2 + right) // 3
    center2 = (left + right*2) // 3
    if f(center1) > f(center2):
        left = center1
    else:
        right = center2

ans = []
for x in range(left, right+1):
    ans.append(f(x))

print("{:.10f}".format(min(ans)))