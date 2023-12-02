n = int(input())

a = n // 16
b = n % 16

abc = ["A", "B", "C", "D", "E", "F"]

if a >= 10:
    idx = a -10
    a = abc[idx]
    
if b >= 10:
    idx = b - 10
    b = abc[idx]

print(str(a)+str(b))
