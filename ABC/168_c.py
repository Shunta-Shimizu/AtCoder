import math
a, b, h, m = map(int, input().split())

h_d = 30*h + 0.5*m
m_d = 6*m

if abs(h_d-m_d) > 180:
    c = 360-abs(h_d-m_d)
else:
    c = abs(h_d-m_d)

# 余弦定理
ans = a**2 + b**2 - 2*a*b*math.cos(math.radians(c))

print(math.sqrt(ans))