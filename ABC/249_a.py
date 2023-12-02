a, b, c, d, e, f, x = map(int, input().split())

p = x // (a + c)
q = x // (d + f)

l1 = b * a * p
rest1 = x - (a + c) * p
if rest1 > 0:
    if rest1 <= a:
        l1 += b * rest1
    else:
        l1 += b * a

l2 = e * d * q
rest2 = x - (d + f) * q
if rest2 > 0:
    if rest2 <= d:
        l2 += e * rest2
    else:
        l2 += e * d

# print(l1, l2)
if l1 > l2:
    print("Takahashi")
elif l1 < l2:
    print("Aoki")
else:
    print("Draw")

