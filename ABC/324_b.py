n = int(input())

def solve(n):
    while n % 2 == 0:
        n //= 2

    while n%3 == 0:
        n //= 3
    
    if n == 1:
        tf = True
    else:
        tf = False
    
    return tf


if solve(n):
    print("Yes")
else:
    print("No")