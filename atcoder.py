# bit全探索
for bit in range(1 << 3):
    print(bit)

print(5 << 2)
print(23 >> 2)

num = 12
n = len(bin(num)[2:])
print(bin(num)[2:])

for i in range(n):
    print(num & (1 << i))
    if num & (1 << i) > 0:
        print("Yes")
    else:
        print("No")

n = int(input())

for bit in range(1 << n):
    patern = []
    print(bit)
    for j in range(n):
        if 1 & (bit >> j):
            patern.append("T")
        else:
            patern.append("F")
    print(patern)