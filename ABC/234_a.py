t = int(input())

f1 = t ** 2 + 2 * t + 3
f2 = f1 + t
f3 = f2 ** 2 + 2 * f2 + 3
f4 = f1 ** 2 + 2 * f1 + 3
ans = (f3 + f4) ** 2 + 2 * (f3 + f4) + 3

print(ans)