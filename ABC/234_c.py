k = int(input())

# k -= 1
bit = 0
i = 0
while True:
    if k // 2 == 0:
        bit += 10**i*k
        break
    else:
        bit += 10**i*(k%2)
        k //= 2
        i += 1

print(bit*2)