import math

a, b = map(int, input().split())

c = math.sqrt(a**2 + b**2)
ans_x = a / c 
ans_y = b /c 

print(ans_x, ans_y)