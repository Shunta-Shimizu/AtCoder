k = int(input())

N = []
for i in range(1 << 10):
    num = ""
    for j in range(10):
        if 1 & (i >> j) == 1:
            num += str(j)
    num = "".join(list(reversed(list(num))))
    if len(num) == 0 or int(num) == 0:
        continue
    else:
        N.append(int(num))

N.sort()
print(N[k-1])
        