n = int(input())

n -= 1
five = 0
i = 0
while True:
    if n // 5 == 0:
        five += 10**i*n
        break
    else:
        if i == 0:
            five += n%5
        else:
            five += 10**i*(n%5)
        n //= 5
        i += 1

print(five*2)