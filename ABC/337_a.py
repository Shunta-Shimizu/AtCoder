n = int(input())

a = 0
b = 0
for _ in range(n):
    x, y = map(int, input().split())
    a += x
    b += y

if a > b:
    print("Takahashi")
elif a == b:
    print("Draw")
else:
    print("Aoki")