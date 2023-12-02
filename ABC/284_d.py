import math

t = int(input())

for _ in range(t):
    n = int(input())
    for i in range(2, int(math.pow(n, 1/3))+1): # n**(1/3)
        if n % i == 0:
            a = i
            if (n//a) % a == 0:
                p = a
                q = n // (a**2)
            else:
                q = a
                p = int(math.sqrt(n//a))
            print(p, q)
            break

        
